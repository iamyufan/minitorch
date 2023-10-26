# from __future__ import annotations

# import random
# from typing import Iterable, List, Optional, Sequence, Tuple, Union

# import numba
# import numpy as np
# import numpy.typing as npt
# from numpy import array, float64
# from typing_extensions import TypeAlias

# from .operators import prod

# MAX_DIMS = 32


# class IndexingError(RuntimeError):
#     "Exception raised for indexing errors."
#     pass


# Storage: TypeAlias = npt.NDArray[np.float64]
# OutIndex: TypeAlias = npt.NDArray[np.int32]
# Index: TypeAlias = npt.NDArray[np.int32]
# Shape: TypeAlias = npt.NDArray[np.int32]
# Strides: TypeAlias = npt.NDArray[np.int32]

# UserIndex: TypeAlias = Sequence[int]
# UserShape: TypeAlias = Sequence[int]
# UserStrides: TypeAlias = Sequence[int]


# def index_to_position(index: Index, strides: Strides) -> int:
#     """
#     Converts a multidimensional tensor `index` into a single-dimensional position in
#     storage based on strides.

#     Args:
#         index : index tuple of ints
#         strides : tensor strides

#     Returns:
#         Position in storage
#     """

#     # TODO: Implement for Task 2.1.
#     pos: int = 0
#     for i, val in enumerate(index):
#         pos += val * strides[i]
#     return pos


# def to_index(ordinal: int, shape: Shape, out_index: OutIndex) -> None:
#     """
#     Convert an `ordinal` to an index in the `shape`.
#     Should ensure that enumerating position 0 ... size of a
#     tensor produces every index exactly once. It
#     may not be the inverse of `index_to_position`.

#     Args:
#         ordinal: ordinal position to convert.
#         shape : tensor shape.
#         out_index : return index corresponding to position.

#     """
#     # TODO: Implement for Task 2.1.
#     cur_orf: int = ordinal + 0
#     for i in range(len(shape) - 1, -1, -1):
#         out_index[i] = int(ordinal % shape[i])
#         # ordinal = ordinal // shape[i]
#         cur_orf //= shape[i]


# def broadcast_index(
#     big_index: Index, big_shape: Shape, shape: Shape, out_index: OutIndex
# ) -> None:
#     """
#     Convert a `big_index` into `big_shape` to a smaller `out_index`
#     into `shape` following broadcasting rules. In this case
#     it may be larger or with more dimensions than the `shape`
#     given. Additional dimensions may need to be mapped to 0 or
#     removed.

#     Args:
#         big_index : multidimensional index of bigger tensor
#         big_shape : tensor shape of bigger tensor
#         shape : tensor shape of smaller tensor
#         out_index : multidimensional index of smaller tensor

#     # Returns:
#     #     None
#     """
#     # TODO: Implement for Task 2.2.
#     dim_diff: int = len(big_shape) - len(shape)
#     for i, val in enumerate(shape):
#         out_index[i] = 0 if val == 1 else big_index[i + dim_diff]


# def shape_broadcast(shape1: UserShape, shape2: UserShape) -> UserShape:
#     """
#     Broadcast two shapes to create a new union shape.

#     Args:
#         shape1 : first shape
#         shape2 : second shape

#     Returns:
#         broadcasted shape

#     Raises:
#         IndexingError : if cannot broadcast
#     """
#     # TODO: Implement for Task 2.2.
#     # Rule 3: extra dimensions of 1 can be implicitly added to the left of the shape.
#     if len(shape1) > len(shape2):
#         shape2 = [1 for _ in range(len(shape1) - len(shape2))] + list(shape2)
#     else:
#         shape1 = [1 for _ in range(len(shape2) - len(shape1))] + list(shape1)
#     # Now, shape1 and shape2 have the same dimension.
#     n_shape: List[int] = []
#     for i in range(len(shape1)):
#         if shape1[i] != shape2[i]:
#             # Rule 1: dimension of size 1 broadcasts with anything
#             if shape1[i] == 1:
#                 n_shape.append(shape2[i])
#             elif shape2[i] == 1:
#                 n_shape.append(shape1[i])
#             else:
#                 raise IndexingError(f"Cannot broadcast {shape1} and {shape2}.")
#         else:
#             n_shape.append(shape1[i])
#     return tuple(n_shape)


# def strides_from_shape(shape: UserShape) -> UserStrides:
#     layout = [1]
#     offset = 1
#     for s in reversed(shape):
#         layout.append(s * offset)
#         offset = s * offset
#     return tuple(reversed(layout[:-1]))


# class TensorData:
#     _storage: Storage
#     _strides: Strides
#     _shape: Shape
#     strides: UserStrides
#     shape: UserShape
#     dims: int

#     def __init__(
#         self,
#         storage: Union[Sequence[float], Storage],
#         shape: UserShape,
#         strides: Optional[UserStrides] = None,
#     ):
#         if isinstance(storage, np.ndarray):
#             self._storage = storage
#         else:
#             self._storage = array(storage, dtype=float64)

#         if strides is None:
#             strides = strides_from_shape(shape)

#         assert isinstance(strides, tuple), "Strides must be tuple"
#         assert isinstance(shape, tuple), "Shape must be tuple"
#         if len(strides) != len(shape):
#             raise IndexingError(f"Len of strides {strides} must match {shape}.")
#         self._strides = array(strides)
#         self._shape = array(shape)
#         self.strides = strides
#         self.dims = len(strides)
#         self.size = int(prod(shape))
#         self.shape = shape
#         assert len(self._storage) == self.size

#     def to_cuda_(self) -> None:  # pragma: no cover
#         if not numba.cuda.is_cuda_array(self._storage):
#             self._storage = numba.cuda.to_device(self._storage)

#     def is_contiguous(self) -> bool:
#         """
#         Check that the layout is contiguous, i.e. outer dimensions have bigger strides than inner dimensions.

#         Returns:
#             bool : True if contiguous
#         """
#         last = 1e9
#         for stride in self._strides:
#             if stride > last:
#                 return False
#             last = stride
#         return True

#     @staticmethod
#     def shape_broadcast(shape_a: UserShape, shape_b: UserShape) -> UserShape:
#         return shape_broadcast(shape_a, shape_b)

#     def index(self, index: Union[int, UserIndex]) -> int:
#         if isinstance(index, int):
#             aindex: Index = array([index])
#         if isinstance(index, tuple):
#             aindex = array(index)

#         # Check for errors
#         if aindex.shape[0] != len(self.shape):
#             raise IndexingError(f"Index {aindex} must be size of {self.shape}.")
#         for i, ind in enumerate(aindex):
#             if ind >= self.shape[i]:
#                 raise IndexingError(f"Index {aindex} out of range {self.shape}.")
#             if ind < 0:
#                 raise IndexingError(f"Negative indexing for {aindex} not supported.")

#         # Call fast indexing.
#         return index_to_position(array(index), self._strides)

#     def indices(self) -> Iterable[UserIndex]:
#         lshape: Shape = array(self.shape)
#         out_index: Index = array(self.shape)
#         for i in range(self.size):
#             to_index(i, lshape, out_index)
#             yield tuple(out_index)

#     def sample(self) -> UserIndex:
#         return tuple((random.randint(0, s - 1) for s in self.shape))

#     def get(self, key: UserIndex) -> float:
#         x: float = self._storage[self.index(key)]
#         return x

#     def set(self, key: UserIndex, val: float) -> None:
#         self._storage[self.index(key)] = val

#     def tuple(self) -> Tuple[Storage, Shape, Strides]:
#         return (self._storage, self._shape, self._strides)

#     def permute(self, *order: int) -> TensorData:
#         """
#         Permute the dimensions of the tensor.

#         Args:
#             order (list): a permutation of the dimensions

#         Returns:
#             New `TensorData` with the same storage and a new dimension order.
#         """
#         assert list(sorted(order)) == list(
#             range(len(self.shape))
#         ), f"Must give a position to each dimension. Shape: {self.shape} Order: {order}"

#         # TODO: Implement for Task 2.1.
#         return TensorData(
#             storage=self._storage,
#             shape=tuple(self.shape[i] for i in order),
#             strides=tuple(self._strides[i] for i in order),
#         )

#     def to_string(self) -> str:
#         s = ""
#         for index in self.indices():
#             l = ""
#             for i in range(len(index) - 1, -1, -1):
#                 if index[i] == 0:
#                     l = "\n%s[" % ("\t" * i) + l
#                 else:
#                     break
#             s += l
#             v = self.get(index)
#             s += f"{v:3.2f}"
#             l = ""
#             for i in range(len(index) - 1, -1, -1):
#                 if index[i] == self.shape[i] - 1:
#                     l += "]"
#                 else:
#                     break
#             if l:
#                 s += l
#             else:
#                 s += " "
#         return s

from __future__ import annotations

import random
from typing import Iterable, Optional, Sequence, Tuple, Union

import numba
import numpy as np
import numpy.typing as npt
from numpy import array, float64
from typing_extensions import TypeAlias

from .operators import prod

MAX_DIMS = 32


class IndexingError(RuntimeError):
    "Exception raised for indexing errors."
    pass


Storage: TypeAlias = npt.NDArray[np.float64]
OutIndex: TypeAlias = npt.NDArray[np.int32]
Index: TypeAlias = npt.NDArray[np.int32]
Shape: TypeAlias = npt.NDArray[np.int32]
Strides: TypeAlias = npt.NDArray[np.int32]

UserIndex: TypeAlias = Sequence[int]
UserShape: TypeAlias = Sequence[int]
UserStrides: TypeAlias = Sequence[int]


def index_to_position(index: Index, strides: Strides) -> int:
    """
    Converts a multidimensional tensor `index` into a single-dimensional position in
    storage based on strides.

    Args:
        index : index tuple of ints
        strides : tensor strides

    Returns:
        Position in storage
    """

    # TODO: Implement for Task 2.1.
    position = 0
    for x, y in zip(index, strides):
        position += x * y
    return position


def to_index(ordinal: int, shape: Shape, out_index: OutIndex) -> None:
    """
    Convert an `ordinal` to an index in the `shape`.
    Should ensure that enumerating position 0 ... size of a
    tensor produces every index exactly once. It
    may not be the inverse of `index_to_position`.

    Args:
        ordinal: ordinal position to convert.
        shape : tensor shape.
        out_index : return index corresponding to position.

    """
    # TODO: Implement for Task 2.1.
    s = int(ordinal)
    for i in range(len(shape) - 1, -1, -1):
        now = shape[i]
        out_index[i] = int(s % now)
        s = s // now
    # stride = int(prod(shape))
    # for i in range(len(shape)):
    #     stride = stride // shape[i]
    #     out_index[i] = ordinal // stride
    #     ordinal %= stride
    # raise NotImplementedError("Need to implement for Task 2.1")


def broadcast_index(
    big_index: Index, big_shape: Shape, shape: Shape, out_index: OutIndex
) -> None:
    """
    Convert a `big_index` into `big_shape` to a smaller `out_index`
    into `shape` following broadcasting rules. In this case
    it may be larger or with more dimensions than the `shape`
    given. Additional dimensions may need to be mapped to 0 or
    removed.

    Args:
        big_index : multidimensional index of bigger tensor
        big_shape : tensor shape of bigger tensor
        shape : tensor shape of smaller tensor
        out_index : multidimensional index of smaller tensor

    Returns:
        None
    """
    # TODO: Implement for Task 2.2.
    start = big_shape.size - shape.size
    for i in range(shape.size):
        out_index[i] = big_index[i + start] if shape[i] != 1 else 0
    return


def shape_broadcast(shape1: UserShape, shape2: UserShape) -> UserShape:
    """
    Broadcast two shapes to create a new union shape.

    Args:
        shape1 : first shape
        shape2 : second shape

    Returns:
        broadcasted shape

    Raises:
        IndexingError : if cannot broadcast
    """
    # TODO: Implement for Task 2.2.
    if len(shape2) > len(shape1):
        shape1, shape2 = shape2, shape1
    shape = list(shape1)
    for i in range(1, len(shape2) + 1):
        if shape1[-i] == 1 or shape2[-i] == 1:
            shape[-i] = max(shape1[-i], shape2[-i])
        elif shape1[-i] != shape2[-i]:
            raise IndexingError(f"{shape1} doesnot match {shape2}")
    return tuple(shape)
    # raise NotImplementedError("Need to implement for Task 2.2")


def strides_from_shape(shape: UserShape) -> UserStrides:
    layout = [1]
    offset = 1
    for s in reversed(shape):
        layout.append(s * offset)
        offset = s * offset
    return tuple(reversed(layout[:-1]))


class TensorData:
    _storage: Storage
    _strides: Strides
    _shape: Shape
    strides: UserStrides
    shape: UserShape
    dims: int

    def __init__(
        self,
        storage: Union[Sequence[float], Storage],
        shape: UserShape,
        strides: Optional[UserStrides] = None,
    ):
        if isinstance(storage, np.ndarray):
            self._storage = storage
        else:
            self._storage = array(storage, dtype=float64)

        if strides is None:
            strides = strides_from_shape(shape)

        assert isinstance(strides, tuple), "Strides must be tuple"
        assert isinstance(shape, tuple), "Shape must be tuple"
        if len(strides) != len(shape):
            raise IndexingError(f"Len of strides {strides} must match {shape}.")
        self._strides = array(strides)
        self._shape = array(shape)
        self.strides = strides
        self.dims = len(strides)
        self.size = int(prod(shape))
        self.shape = shape
        assert len(self._storage) == self.size

    def to_cuda_(self) -> None:  # pragma: no cover
        if not numba.cuda.is_cuda_array(self._storage):
            self._storage = numba.cuda.to_device(self._storage)

    def is_contiguous(self) -> bool:
        """
        Check that the layout is contiguous, i.e. outer dimensions have bigger strides than inner dimensions.

        Returns:
            bool : True if contiguous
        """
        last = 1e9
        for stride in self._strides:
            if stride > last:
                return False
            last = stride
        return True

    @staticmethod
    def shape_broadcast(shape_a: UserShape, shape_b: UserShape) -> UserShape:
        return shape_broadcast(shape_a, shape_b)

    def index(self, index: Union[int, UserIndex]) -> int:
        if isinstance(index, int):
            aindex: Index = array([index])
        if isinstance(index, tuple):
            aindex = array(index)

        # Check for errors
        if aindex.shape[0] != len(self.shape):
            raise IndexingError(f"Index {aindex} must be size of {self.shape}.")
        for i, ind in enumerate(aindex):
            if ind >= self.shape[i]:
                raise IndexingError(f"Index {aindex} out of range {self.shape}.")
            if ind < 0:
                raise IndexingError(f"Negative indexing for {aindex} not supported.")

        # Call fast indexing.
        return index_to_position(array(index), self._strides)

    def indices(self) -> Iterable[UserIndex]:
        lshape: Shape = array(self.shape)
        out_index: Index = array(self.shape)
        for i in range(self.size):
            to_index(i, lshape, out_index)
            yield tuple(out_index)

    def sample(self) -> UserIndex:
        return tuple((random.randint(0, s - 1) for s in self.shape))

    def get(self, key: UserIndex) -> float:
        x: float = self._storage[self.index(key)]
        return x

    def set(self, key: UserIndex, val: float) -> None:
        self._storage[self.index(key)] = val

    def tuple(self) -> Tuple[Storage, Shape, Strides]:
        return (self._storage, self._shape, self._strides)

    def permute(self, *order: int) -> TensorData:
        """
        Permute the dimensions of the tensor.

        Args:
            order (list): a permutation of the dimensions

        Returns:
            New `TensorData` with the same storage and a new dimension order.
        """
        assert list(sorted(order)) == list(
            range(len(self.shape))
        ), f"Must give a position to each dimension. Shape: {self.shape} Order: {order}"

        # TODO: Implement for Task 2.1.
        shape = tuple(self.shape[i] for i in order)
        strides = tuple(self.strides[i] for i in order)
        return TensorData(self._storage, shape, strides)
        # raise NotImplementedError("Need to implement for Task 2.1")

    def to_string(self) -> str:
        s = ""
        for index in self.indices():
            l = ""
            for i in range(len(index) - 1, -1, -1):
                if index[i] == 0:
                    l = "\n%s[" % ("\t" * i) + l
                else:
                    break
            s += l
            v = self.get(index)
            s += f"{v:3.2f}"
            l = ""
            for i in range(len(index) - 1, -1, -1):
                if index[i] == self.shape[i] - 1:
                    l += "]"
                else:
                    break
            if l:
                s += l
            else:
                s += " "
        return s