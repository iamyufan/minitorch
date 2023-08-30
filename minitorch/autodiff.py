from dataclasses import dataclass
from typing import Any, Iterable, List, Tuple

from typing_extensions import Protocol

# ## Task 1.1
# Central Difference calculation


def central_difference(f: Any, *vals: Any, arg: int = 0, epsilon: float = 1e-6) -> Any:
    r"""
    Computes an approximation to the derivative of `f` with respect to one arg.

    See :doc:`derivative` or https://en.wikipedia.org/wiki/Finite_difference for more details.

    Args:
        f : arbitrary function from n-scalar args to one value
        *vals : n-float values $x_0 \ldots x_{n-1}$
        arg : the number $i$ of the arg to compute the derivative
        epsilon : a small constant

    Returns:
        An approximation of $f'_i(x_0, \ldots, x_{n-1})$
    """
    # TODO: Implement for Task 1.1.
    vals: Iterable[Any] = list(vals)
    vals[arg] += epsilon
    func_val1: Any = f(*vals)
    vals[arg] -= 2 * epsilon
    func_val2: Any = f(*vals)

    return (func_val1 - func_val2) / (2 * epsilon)


variable_count = 1


class Variable(Protocol):
    def accumulate_derivative(self, x: Any) -> None:
        pass

    @property
    def unique_id(self) -> int:
        pass

    def is_leaf(self) -> bool:
        pass

    def is_constant(self) -> bool:
        pass

    @property
    def parents(self) -> Iterable["Variable"]:
        pass

    def chain_rule(self, d_output: Any) -> Iterable[Tuple["Variable", Any]]:
        pass


def topological_sort(variable: Variable) -> Iterable[Variable]:
    """
    Computes the topological order of the computation graph.

    Args:
        variable: The right-most variable

    Returns:
        Non-constant Variables in topological order starting from the right.
    """
    # TODO: Implement for Task 1.4.
    order: Iterable[Variable] = []
    visited: List[int] = []
    dfs(variable, visited, order)
    return order


def dfs(variable: Variable, visited: List[Variable], order: Iterable[Variable]) -> None:
    """
    Depth-first search for topological sort.

    Args:
        variable (Variable): The right-most variable
        visited (List[Variable]): List of visited variables
        order (Iterable[Variable]): Non-constant Variables in topological order starting from the right.
    """

    if variable.unique_id in visited:
        return
    if not variable.is_leaf():
        for parent in variable.parents:
            dfs(parent, visited, order)
    visited.append(variable.unique_id)
    order.insert(0, variable)


def backpropagate(variable: Variable, deriv: Any) -> None:
    """
    Runs backpropagation on the computation graph in order to
    compute derivatives for the leave nodes.

    Args:
        variable: The right-most variable
        deriv  : Its derivative that we want to propagate backward to the leaves.

    No return. Should write to its results to the derivative values of each leaf through `accumulate_derivative`.
    """
    # TODO: Implement for Task 1.4.
    ordered_vars: Iterable[Variable] = topological_sort(variable)
    # Create a dictionary to store the derivative of each variable
    deriv_dict: dict = {var.unique_id: 0 for var in ordered_vars}
    deriv_dict[variable.unique_id] = deriv

    for var in ordered_vars:
        if var.is_leaf():
            var.accumulate_derivative(deriv_dict[var.unique_id])
        else:
            for parent, deriv in var.chain_rule(deriv_dict[var.unique_id]):
                if parent.unique_id in deriv_dict:
                    deriv_dict[parent.unique_id] += deriv
                else:
                    deriv_dict[parent.unique_id] = deriv


@dataclass
class Context:
    """
    Context class is used by `Function` to store information during the forward pass.
    """

    no_grad: bool = False
    saved_values: Tuple[Any, ...] = ()

    def save_for_backward(self, *values: Any) -> None:
        "Store the given `values` if they need to be used during backpropagation."
        if self.no_grad:
            return
        self.saved_values = values

    @property
    def saved_tensors(self) -> Tuple[Any, ...]:
        return self.saved_values
