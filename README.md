# Module 2: Tensor

<img src="https://minitorch.github.io/minitorch.svg" width="50%">

## Task 5: Training

### Simple

Parameters

|           | Size of hidden layer | Learning rate | Number of epochs |
| --------- | -------------------- | ------------- | ---------------- |
| parameter | 3                    | 0.1           | 700              |

Training results

- Time per epoch: 0.062s

![Simple](./img/m2/simple-1.png)

![Simple Loss](./img/m2/simple-2.png)

Training log

```bash
Epoch: 0/700, loss: 0, correct: 0
Epoch: 10/700, loss: 41.50248863798288, correct: 21
Epoch: 20/700, loss: 36.31631822946457, correct: 21
Epoch: 30/700, loss: 34.92400111284607, correct: 21
Epoch: 40/700, loss: 34.47123224657338, correct: 29
Epoch: 50/700, loss: 34.21710102990968, correct: 29
Epoch: 60/700, loss: 34.02501667714936, correct: 29
Epoch: 70/700, loss: 33.85159188318461, correct: 29
Epoch: 80/700, loss: 33.676868373019474, correct: 29
Epoch: 90/700, loss: 33.486722326523136, correct: 29
Epoch: 100/700, loss: 33.2694904872939, correct: 29
Epoch: 110/700, loss: 33.01201273503461, correct: 29
Epoch: 120/700, loss: 32.69731385699528, correct: 29
Epoch: 130/700, loss: 32.3027830728012, correct: 29
Epoch: 140/700, loss: 31.798904223036182, correct: 29
Epoch: 150/700, loss: 31.14530595553706, correct: 33
Epoch: 160/700, loss: 30.288692453373486, correct: 37
Epoch: 170/700, loss: 29.17522150633598, correct: 43
Epoch: 180/700, loss: 27.756338575675503, correct: 46
Epoch: 190/700, loss: 26.02855351464764, correct: 50
Epoch: 200/700, loss: 24.018768485782736, correct: 50
Epoch: 210/700, loss: 21.836784232513384, correct: 50
Epoch: 220/700, loss: 19.6206852914555, correct: 50
Epoch: 230/700, loss: 17.437697292721516, correct: 50
Epoch: 240/700, loss: 15.402991842274005, correct: 50
Epoch: 250/700, loss: 13.584807374247722, correct: 50
Epoch: 260/700, loss: 11.982226770854535, correct: 50
Epoch: 270/700, loss: 10.595503701784237, correct: 50
Epoch: 280/700, loss: 9.406896432168283, correct: 50
Epoch: 290/700, loss: 8.391252650535167, correct: 50
Epoch: 300/700, loss: 7.526548032875611, correct: 50
Epoch: 310/700, loss: 6.803235284381629, correct: 50
Epoch: 320/700, loss: 6.187102099976993, correct: 50
Epoch: 330/700, loss: 5.655540231011341, correct: 50
Epoch: 340/700, loss: 5.194940152297081, correct: 50
Epoch: 350/700, loss: 4.796726896776214, correct: 50
Epoch: 360/700, loss: 4.454636566786966, correct: 50
Epoch: 370/700, loss: 4.152555774714047, correct: 50
Epoch: 380/700, loss: 3.8844284684733634, correct: 50
Epoch: 390/700, loss: 3.6474664165245447, correct: 50
Epoch: 400/700, loss: 3.435071191764164, correct: 50
Epoch: 410/700, loss: 3.2440606909816427, correct: 50
Epoch: 420/700, loss: 3.071561491973418, correct: 50
Epoch: 430/700, loss: 2.914889154826596, correct: 50
Epoch: 440/700, loss: 2.7721147486289435, correct: 50
Epoch: 450/700, loss: 2.6418223973366612, correct: 50
Epoch: 460/700, loss: 2.5228489000196728, correct: 50
Epoch: 470/700, loss: 2.4135597831418543, correct: 50
Epoch: 480/700, loss: 2.312739582176322, correct: 50
Epoch: 490/700, loss: 2.219797697042586, correct: 50
Epoch: 500/700, loss: 2.13400348754432, correct: 50
Epoch: 510/700, loss: 2.054035787804819, correct: 50
Epoch: 520/700, loss: 1.9792570281149102, correct: 50
Epoch: 530/700, loss: 1.909178526433619, correct: 50
Epoch: 540/700, loss: 1.8434852168334828, correct: 50
Epoch: 550/700, loss: 1.7816860663313878, correct: 50
Epoch: 560/700, loss: 1.7234242133389805, correct: 50
Epoch: 570/700, loss: 1.6684147859693617, correct: 50
Epoch: 580/700, loss: 1.6163817024900027, correct: 50
Epoch: 590/700, loss: 1.5670857197468067, correct: 50
Epoch: 600/700, loss: 1.5203152816578185, correct: 50
Epoch: 610/700, loss: 1.4758802955792165, correct: 50
Epoch: 620/700, loss: 1.4336204168750137, correct: 50
Epoch: 630/700, loss: 1.3933679469840325, correct: 50
Epoch: 640/700, loss: 1.3549831023104941, correct: 50
Epoch: 650/700, loss: 1.318339040010424, correct: 50
Epoch: 660/700, loss: 1.2833203869563852, correct: 50
Epoch: 670/700, loss: 1.2498219726501534, correct: 50
Epoch: 680/700, loss: 1.217747723419944, correct: 50
Epoch: 690/700, loss: 1.1870096949846645, correct: 50
Epoch: 700/700, loss: 1.157527224054579, correct: 50
```

### Diag

Parameters

|           | Size of hidden layer | Learning rate | Number of epochs |
| --------- | -------------------- | ------------- | ---------------- |
| parameter | 3                    | 0.1           | 600              |

Training results

- Time per epoch: 0.063s

![Diag](./img/m2/diag-1.png)

![Diag Loss](./img/m2/diag-2.png)

Training log

```bash
Epoch: 0/600, loss: 0, correct: 0
Epoch: 10/600, loss: 27.67989726575394, correct: 47
Epoch: 20/600, loss: 15.031558194179444, correct: 45
Epoch: 30/600, loss: 13.030605819479957, correct: 45
Epoch: 40/600, loss: 12.569009022875196, correct: 45
Epoch: 50/600, loss: 12.28018076798621, correct: 45
Epoch: 60/600, loss: 12.004073805131409, correct: 45
Epoch: 70/600, loss: 11.719152962184793, correct: 45
Epoch: 80/600, loss: 11.419845638993754, correct: 45
Epoch: 90/600, loss: 11.10559182097841, correct: 45
Epoch: 100/600, loss: 10.776843469780184, correct: 45
Epoch: 110/600, loss: 10.435636331275607, correct: 45
Epoch: 120/600, loss: 10.084036856203117, correct: 45
Epoch: 130/600, loss: 9.722607075494604, correct: 45
Epoch: 140/600, loss: 9.354597935318587, correct: 45
Epoch: 150/600, loss: 8.982360854060596, correct: 45
Epoch: 160/600, loss: 8.608046798776995, correct: 45
Epoch: 170/600, loss: 8.234749435370544, correct: 45
Epoch: 180/600, loss: 7.865356809605689, correct: 45
Epoch: 190/600, loss: 7.5027925606741865, correct: 45
Epoch: 200/600, loss: 7.149662945062035, correct: 46
Epoch: 210/600, loss: 6.808059465329838, correct: 46
Epoch: 220/600, loss: 6.479706437459847, correct: 47
Epoch: 230/600, loss: 6.165868451795294, correct: 47
Epoch: 240/600, loss: 5.904453440692729, correct: 47
Epoch: 250/600, loss: 5.691854975968948, correct: 47
Epoch: 260/600, loss: 5.489237525002306, correct: 48
Epoch: 270/600, loss: 5.294687441981102, correct: 48
Epoch: 280/600, loss: 5.109518672647591, correct: 48
Epoch: 290/600, loss: 4.949326539357826, correct: 48
Epoch: 300/600, loss: 4.808876912533211, correct: 48
Epoch: 310/600, loss: 4.680893921309398, correct: 48
Epoch: 320/600, loss: 4.5581975838864475, correct: 48
Epoch: 330/600, loss: 4.439752399467426, correct: 48
Epoch: 340/600, loss: 4.325419462339773, correct: 48
Epoch: 350/600, loss: 4.215062461390343, correct: 49
Epoch: 360/600, loss: 4.108550348107263, correct: 49
Epoch: 370/600, loss: 4.005751798514593, correct: 49
Epoch: 380/600, loss: 3.906514526166758, correct: 49
Epoch: 390/600, loss: 3.8107034621081377, correct: 50
Epoch: 400/600, loss: 3.719734368127981, correct: 50
Epoch: 410/600, loss: 3.636505680319877, correct: 50
Epoch: 420/600, loss: 3.5567822609328084, correct: 50
Epoch: 430/600, loss: 3.4801048256873224, correct: 50
Epoch: 440/600, loss: 3.409726612759962, correct: 50
Epoch: 450/600, loss: 3.3424105294872795, correct: 50
Epoch: 460/600, loss: 3.277447088713388, correct: 50
Epoch: 470/600, loss: 3.2151198932118588, correct: 50
Epoch: 480/600, loss: 3.1556545040498483, correct: 50
Epoch: 490/600, loss: 3.098053002538095, correct: 50
Epoch: 500/600, loss: 3.0419881591054714, correct: 50
Epoch: 510/600, loss: 2.987400904433333, correct: 50
Epoch: 520/600, loss: 2.9342397952225787, correct: 50
Epoch: 530/600, loss: 2.8824556629708296, correct: 50
Epoch: 540/600, loss: 2.832001451081918, correct: 50
Epoch: 550/600, loss: 2.7828321192249046, correct: 50
Epoch: 560/600, loss: 2.734904546966283, correct: 50
Epoch: 570/600, loss: 2.6876800575523507, correct: 50
Epoch: 580/600, loss: 2.6397618854407825, correct: 50
Epoch: 590/600, loss: 2.593097693014048, correct: 50
Epoch: 600/600, loss: 2.540400246596195, correct: 50
```

### Split

Parameters

|           | Size of hidden layer | Learning rate | Number of epochs |
| --------- | -------------------- | ------------- | ---------------- |
| parameter | 3                    | 0.1           | 800              |

Training results

- Time per epoch: 0.062s

![Split](./img/m2/split-1.png)

![Split Loss](./img/m2/split-2.png)

Training log

```bash
Epoch: 0/800, loss: 0, correct: 0
Epoch: 10/800, loss: 35.1372325431047, correct: 26
Epoch: 20/800, loss: 34.20277880348396, correct: 26
Epoch: 30/800, loss: 33.84441333855868, correct: 27
Epoch: 40/800, loss: 33.68899350149333, correct: 35
Epoch: 50/800, loss: 33.59615018629735, correct: 35
Epoch: 60/800, loss: 33.51952386736619, correct: 32
Epoch: 70/800, loss: 33.44394982880903, correct: 32
Epoch: 80/800, loss: 33.36230284386042, correct: 32
Epoch: 90/800, loss: 33.271078182812836, correct: 32
Epoch: 100/800, loss: 33.173744758860565, correct: 32
Epoch: 110/800, loss: 33.06961413466836, correct: 32
Epoch: 120/800, loss: 32.956857142777245, correct: 32
Epoch: 130/800, loss: 32.83661551651286, correct: 32
Epoch: 140/800, loss: 32.70936807811026, correct: 32
Epoch: 150/800, loss: 32.570945508743606, correct: 32
Epoch: 160/800, loss: 32.417843096205715, correct: 32
Epoch: 170/800, loss: 32.25576906753061, correct: 33
Epoch: 180/800, loss: 32.08668099510918, correct: 37
Epoch: 190/800, loss: 31.907312714794813, correct: 38
Epoch: 200/800, loss: 31.71635676129443, correct: 39
Epoch: 210/800, loss: 31.513772875023214, correct: 44
Epoch: 220/800, loss: 31.30171287808461, correct: 44
Epoch: 230/800, loss: 31.08036505314927, correct: 45
Epoch: 240/800, loss: 30.847852548858125, correct: 45
Epoch: 250/800, loss: 30.601861887468928, correct: 46
Epoch: 260/800, loss: 30.344471509179343, correct: 46
Epoch: 270/800, loss: 30.073558589205003, correct: 46
Epoch: 280/800, loss: 29.789398645683313, correct: 46
Epoch: 290/800, loss: 29.49117353967811, correct: 46
Epoch: 300/800, loss: 29.17885737171285, correct: 46
Epoch: 310/800, loss: 28.853109042521567, correct: 45
Epoch: 320/800, loss: 28.518150410498976, correct: 45
Epoch: 330/800, loss: 28.15903677774181, correct: 45
Epoch: 340/800, loss: 27.671625200889064, correct: 44
Epoch: 350/800, loss: 27.11706428087733, correct: 45
Epoch: 360/800, loss: 26.52854466049474, correct: 45
Epoch: 370/800, loss: 25.9634235334256, correct: 45
Epoch: 380/800, loss: 25.419876781298026, correct: 46
Epoch: 390/800, loss: 24.8785509618284, correct: 46
Epoch: 400/800, loss: 24.275279505060205, correct: 46
Epoch: 410/800, loss: 23.696080433291897, correct: 46
Epoch: 420/800, loss: 23.098763611403086, correct: 46
Epoch: 430/800, loss: 22.509835390035693, correct: 45
Epoch: 440/800, loss: 21.929278656901314, correct: 45
Epoch: 450/800, loss: 21.3341477306649, correct: 45
Epoch: 460/800, loss: 20.715772181710054, correct: 45
Epoch: 470/800, loss: 20.112431588056264, correct: 45
Epoch: 480/800, loss: 19.50415907424774, correct: 46
Epoch: 490/800, loss: 18.917721799783546, correct: 46
Epoch: 500/800, loss: 18.347126858962216, correct: 46
Epoch: 510/800, loss: 17.80100175596908, correct: 46
Epoch: 520/800, loss: 17.27197523471437, correct: 46
Epoch: 530/800, loss: 16.754481383836286, correct: 46
Epoch: 540/800, loss: 16.25287186609402, correct: 46
Epoch: 550/800, loss: 15.76506384188441, correct: 46
Epoch: 560/800, loss: 15.304366635682422, correct: 46
Epoch: 570/800, loss: 14.858563959522595, correct: 47
Epoch: 580/800, loss: 14.42409137601907, correct: 47
Epoch: 590/800, loss: 14.00187375076616, correct: 48
Epoch: 600/800, loss: 13.592349582804978, correct: 48
Epoch: 610/800, loss: 13.195976762659468, correct: 48
Epoch: 620/800, loss: 12.813388466565515, correct: 48
Epoch: 630/800, loss: 12.450794362125764, correct: 48
Epoch: 640/800, loss: 12.107673501933641, correct: 48
Epoch: 650/800, loss: 11.790757472644337, correct: 48
Epoch: 660/800, loss: 11.489197124624152, correct: 48
Epoch: 670/800, loss: 11.198468415987918, correct: 48
Epoch: 680/800, loss: 10.924094575479838, correct: 48
Epoch: 690/800, loss: 10.668738391463235, correct: 48
Epoch: 700/800, loss: 10.423363912936548, correct: 48
Epoch: 710/800, loss: 10.188425705791339, correct: 48
Epoch: 720/800, loss: 9.961208603171151, correct: 48
Epoch: 730/800, loss: 9.742045771311313, correct: 48
Epoch: 740/800, loss: 9.531203925814056, correct: 48
Epoch: 750/800, loss: 9.327042972668668, correct: 48
Epoch: 760/800, loss: 9.132171717598816, correct: 48
Epoch: 770/800, loss: 8.941729129622061, correct: 48
Epoch: 780/800, loss: 8.75966050757842, correct: 48
Epoch: 790/800, loss: 8.590247976227374, correct: 48
Epoch: 800/800, loss: 8.42788350623998, correct: 48
```

### Xor

Parameters

|           | Size of hidden layer | Learning rate | Number of epochs |
| --------- | -------------------- | ------------- | ---------------- |
| parameter | 8                    | 0.5           | 900              |

Training results

- Time per epoch: 0.216s

![Xor](./img/m2/xor-1.png)

![Xor Loss](./img/m2/xor-2.png)

Training log

```bash
Epoch: 0/900, loss: 0, correct: 0
Epoch: 10/900, loss: 29.46862202257828, correct: 36
Epoch: 20/900, loss: 27.9337994141294, correct: 36
Epoch: 30/900, loss: 26.963275234600687, correct: 39
Epoch: 40/900, loss: 28.750771572672, correct: 36
Epoch: 50/900, loss: 23.101622848892482, correct: 41
Epoch: 60/900, loss: 20.722376570992573, correct: 42
Epoch: 70/900, loss: 19.971341987878613, correct: 42
Epoch: 80/900, loss: 15.558975452033794, correct: 44
Epoch: 90/900, loss: 14.484002437242406, correct: 47
Epoch: 100/900, loss: 19.534118840256212, correct: 40
Epoch: 110/900, loss: 14.335931220810242, correct: 44
Epoch: 120/900, loss: 13.657264773138564, correct: 44
Epoch: 130/900, loss: 13.476204742196188, correct: 43
Epoch: 140/900, loss: 12.887795185579265, correct: 43
Epoch: 150/900, loss: 11.821676007713744, correct: 44
Epoch: 160/900, loss: 10.253773523880058, correct: 45
Epoch: 170/900, loss: 9.063597685843915, correct: 47
Epoch: 180/900, loss: 10.249614010096693, correct: 46
Epoch: 190/900, loss: 16.52755499149607, correct: 43
Epoch: 200/900, loss: 10.183053089546899, correct: 44
Epoch: 210/900, loss: 9.21592496326576, correct: 45
Epoch: 220/900, loss: 9.002185920407122, correct: 44
Epoch: 230/900, loss: 8.267129403274025, correct: 47
Epoch: 240/900, loss: 8.56786160656515, correct: 46
Epoch: 250/900, loss: 7.622035996397223, correct: 47
Epoch: 260/900, loss: 7.583600342177728, correct: 47
Epoch: 270/900, loss: 8.052670543815573, correct: 46
Epoch: 280/900, loss: 8.545963682352726, correct: 45
Epoch: 290/900, loss: 10.583065609245828, correct: 44
Epoch: 300/900, loss: 12.086854870880199, correct: 44
Epoch: 310/900, loss: 6.631889765462148, correct: 47
Epoch: 320/900, loss: 6.468076331481887, correct: 48
Epoch: 330/900, loss: 5.660541903359598, correct: 48
Epoch: 340/900, loss: 6.1071103702692575, correct: 47
Epoch: 350/900, loss: 5.869461879211359, correct: 48
Epoch: 360/900, loss: 12.36094199494515, correct: 43
Epoch: 370/900, loss: 8.17474625848713, correct: 47
Epoch: 380/900, loss: 7.782617302683845, correct: 46
Epoch: 390/900, loss: 6.885020367428006, correct: 47
Epoch: 400/900, loss: 5.410761295080726, correct: 48
Epoch: 410/900, loss: 6.675040524551362, correct: 46
Epoch: 420/900, loss: 10.514299775938321, correct: 46
Epoch: 430/900, loss: 12.45803982767832, correct: 46
Epoch: 440/900, loss: 5.46681714673899, correct: 47
Epoch: 450/900, loss: 5.826142152880877, correct: 47
Epoch: 460/900, loss: 7.2553061774577134, correct: 46
Epoch: 470/900, loss: 7.160665191877258, correct: 47
Epoch: 480/900, loss: 4.520755491917096, correct: 49
Epoch: 490/900, loss: 5.0878641262388555, correct: 48
Epoch: 500/900, loss: 7.397058680823627, correct: 45
Epoch: 510/900, loss: 6.043151131257391, correct: 48
Epoch: 520/900, loss: 6.601675575273849, correct: 46
Epoch: 530/900, loss: 8.223845136715097, correct: 45
Epoch: 540/900, loss: 5.383549866416397, correct: 47
Epoch: 550/900, loss: 3.5355499695655874, correct: 50
Epoch: 560/900, loss: 4.119208800817654, correct: 48
Epoch: 570/900, loss: 4.606547346049013, correct: 48
Epoch: 580/900, loss: 5.1061442727487245, correct: 48
Epoch: 590/900, loss: 13.31593574731712, correct: 42
Epoch: 600/900, loss: 7.672911132520378, correct: 46
Epoch: 610/900, loss: 3.7578834653941926, correct: 50
Epoch: 620/900, loss: 3.2916219740676818, correct: 50
Epoch: 630/900, loss: 3.165189454756024, correct: 50
Epoch: 640/900, loss: 2.659789581461949, correct: 50
Epoch: 650/900, loss: 2.5228260225856154, correct: 50
Epoch: 660/900, loss: 8.857293006129952, correct: 45
Epoch: 670/900, loss: 8.329265689842803, correct: 46
Epoch: 680/900, loss: 3.370962078718966, correct: 50
Epoch: 690/900, loss: 2.375352336847335, correct: 50
Epoch: 700/900, loss: 2.609097737210271, correct: 50
Epoch: 710/900, loss: 11.020370288851659, correct: 45
Epoch: 720/900, loss: 2.998471125740831, correct: 50
Epoch: 730/900, loss: 1.9364661075482295, correct: 50
Epoch: 740/900, loss: 1.9396046280259966, correct: 50
Epoch: 750/900, loss: 7.4299120160645264, correct: 45
Epoch: 760/900, loss: 1.6949280882078683, correct: 50
Epoch: 770/900, loss: 1.4740280147019242, correct: 50
Epoch: 780/900, loss: 1.3899251245363597, correct: 50
Epoch: 790/900, loss: 1.367091948036271, correct: 50
Epoch: 800/900, loss: 1.4117343211384985, correct: 50
Epoch: 810/900, loss: 1.9642947177056196, correct: 50
Epoch: 820/900, loss: 3.256382796117901, correct: 49
Epoch: 830/900, loss: 3.5180919298992595, correct: 49
Epoch: 840/900, loss: 4.7716443461823195, correct: 47
Epoch: 850/900, loss: 5.025009195820685, correct: 46
Epoch: 860/900, loss: 1.567927192103266, correct: 50
Epoch: 870/900, loss: 1.187373489396747, correct: 50
Epoch: 880/900, loss: 1.0868860978454928, correct: 50
Epoch: 890/900, loss: 1.0216084279775943, correct: 50
Epoch: 900/900, loss: 0.9847695112338157, correct: 50
```

### Circle

Parameters

|           | Size of hidden layer | Learning rate | Number of epochs |
| --------- | -------------------- | ------------- | ---------------- |
| parameter | 7                    | 0.5           | 900              |

Training results

- Time per epoch: 0.176s

![Circle](./img/m2/circle-1.png)

![Circle Loss](./img/m2/circle-2.png)

Training log

```bash
Epoch: 0/900, loss: 0, correct: 0
Epoch: 10/900, loss: 33.74587619341894, correct: 30
Epoch: 20/900, loss: 33.67980506720361, correct: 30
Epoch: 30/900, loss: 33.654509976495106, correct: 30
Epoch: 40/900, loss: 33.63639172404643, correct: 30
Epoch: 50/900, loss: 33.612114625619824, correct: 30
Epoch: 60/900, loss: 33.5817602894846, correct: 30
Epoch: 70/900, loss: 33.55469422848879, correct: 30
Epoch: 80/900, loss: 33.525525613745984, correct: 30
Epoch: 90/900, loss: 33.4937828012442, correct: 30
Epoch: 100/900, loss: 33.45958723296899, correct: 30
Epoch: 110/900, loss: 33.42137637284692, correct: 30
Epoch: 120/900, loss: 33.3789800331215, correct: 30
Epoch: 130/900, loss: 33.33140032822648, correct: 30
Epoch: 140/900, loss: 33.277101045359714, correct: 30
Epoch: 150/900, loss: 33.216863357817985, correct: 30
Epoch: 160/900, loss: 33.14665897404298, correct: 30
Epoch: 170/900, loss: 33.06699936709744, correct: 30
Epoch: 180/900, loss: 32.975283922847375, correct: 30
Epoch: 190/900, loss: 32.868127584258175, correct: 30
Epoch: 200/900, loss: 32.74026695161896, correct: 30
Epoch: 210/900, loss: 32.592153536514026, correct: 30
Epoch: 220/900, loss: 32.41490474653907, correct: 30
Epoch: 230/900, loss: 32.203393748328054, correct: 30
Epoch: 240/900, loss: 31.94662547184618, correct: 30
Epoch: 250/900, loss: 31.668329045655213, correct: 30
Epoch: 260/900, loss: 31.333611681119883, correct: 30
Epoch: 270/900, loss: 30.950188983144095, correct: 30
Epoch: 280/900, loss: 30.49982872661795, correct: 30
Epoch: 290/900, loss: 29.9487434283953, correct: 33
Epoch: 300/900, loss: 29.312174729667156, correct: 33
Epoch: 310/900, loss: 28.559200182094166, correct: 34
Epoch: 320/900, loss: 27.751202810740292, correct: 36
Epoch: 330/900, loss: 26.843019022076238, correct: 38
Epoch: 340/900, loss: 25.870181517004408, correct: 40
Epoch: 350/900, loss: 24.928596293154712, correct: 41
Epoch: 360/900, loss: 24.292283508197233, correct: 40
Epoch: 370/900, loss: 24.435598716921984, correct: 36
Epoch: 380/900, loss: 24.204797631515067, correct: 36
Epoch: 390/900, loss: 24.093742335980014, correct: 36
Epoch: 400/900, loss: 24.552101718485368, correct: 37
Epoch: 410/900, loss: 24.603713110061687, correct: 37
Epoch: 420/900, loss: 24.727830341839553, correct: 37
Epoch: 430/900, loss: 24.36933203006961, correct: 36
Epoch: 440/900, loss: 23.965840451923572, correct: 37
Epoch: 450/900, loss: 23.856676756245783, correct: 37
Epoch: 460/900, loss: 23.537438484001424, correct: 37
Epoch: 470/900, loss: 23.036119187526666, correct: 39
Epoch: 480/900, loss: 21.683435725749575, correct: 39
Epoch: 490/900, loss: 22.86199299250165, correct: 39
Epoch: 500/900, loss: 22.691755656038833, correct: 39
Epoch: 510/900, loss: 22.217299849469338, correct: 39
Epoch: 520/900, loss: 21.20201075778088, correct: 39
Epoch: 530/900, loss: 21.858016748866966, correct: 39
Epoch: 540/900, loss: 22.155897608463295, correct: 39
Epoch: 550/900, loss: 20.72812457208465, correct: 39
Epoch: 560/900, loss: 18.490777002091384, correct: 39
Epoch: 570/900, loss: 18.61660737360148, correct: 39
Epoch: 580/900, loss: 21.75670337937457, correct: 39
Epoch: 590/900, loss: 24.7640048543429, correct: 37
Epoch: 600/900, loss: 19.55693731792143, correct: 39
Epoch: 610/900, loss: 17.979607853990732, correct: 40
Epoch: 620/900, loss: 18.80821802704264, correct: 39
Epoch: 630/900, loss: 21.975416728485907, correct: 39
Epoch: 640/900, loss: 21.866920189555447, correct: 39
Epoch: 650/900, loss: 18.947985755139054, correct: 39
Epoch: 660/900, loss: 18.678493311071016, correct: 39
Epoch: 670/900, loss: 19.27535779470615, correct: 39
Epoch: 680/900, loss: 20.544680428149032, correct: 39
Epoch: 690/900, loss: 20.242741118368397, correct: 39
Epoch: 700/900, loss: 18.99597438350525, correct: 39
Epoch: 710/900, loss: 18.747012611160997, correct: 39
Epoch: 720/900, loss: 19.86868869700804, correct: 39
Epoch: 730/900, loss: 20.0178364495819, correct: 39
Epoch: 740/900, loss: 19.515554594475553, correct: 39
Epoch: 750/900, loss: 18.829428109077558, correct: 39
Epoch: 760/900, loss: 19.18727945763228, correct: 39
Epoch: 770/900, loss: 19.596193407596402, correct: 39
Epoch: 780/900, loss: 19.37046640568239, correct: 39
Epoch: 790/900, loss: 19.13695280399404, correct: 39
Epoch: 800/900, loss: 19.025587812860834, correct: 39
Epoch: 810/900, loss: 18.2048929414956, correct: 40
Epoch: 820/900, loss: 18.212006641907863, correct: 40
Epoch: 830/900, loss: 19.720890479119586, correct: 39
Epoch: 840/900, loss: 19.38840995043476, correct: 39
Epoch: 850/900, loss: 18.89730570297293, correct: 39
Epoch: 860/900, loss: 18.602612005395937, correct: 40
Epoch: 870/900, loss: 18.548963446788125, correct: 40
Epoch: 880/900, loss: 18.586714571633525, correct: 39
Epoch: 890/900, loss: 18.152908957588895, correct: 40
Epoch: 900/900, loss: 18.20247517019764, correct: 40
```

### Spiral

Parameters

|           | Size of hidden layer | Learning rate | Number of epochs |
| --------- | -------------------- | ------------- | ---------------- |
| parameter | 16                   | 0.5           | 800              |

Training results

- Time per epoch: 1.222s

![Spiral](./img/m2/spiral-1.png)

![Spiral Loss](./img/m2/spiral-2.png)

Training log

```bash
Epoch: 0/800, loss: 0, correct: 0
Epoch: 10/800, loss: 68.68619028884403, correct: 55
Epoch: 20/800, loss: 68.3561667459355, correct: 59
Epoch: 30/800, loss: 68.09172983040025, correct: 59
Epoch: 40/800, loss: 67.87063863954977, correct: 58
Epoch: 50/800, loss: 67.68408089084281, correct: 58
Epoch: 60/800, loss: 67.52662377239982, correct: 60
Epoch: 70/800, loss: 67.40105954589376, correct: 59
Epoch: 80/800, loss: 67.302605623504, correct: 59
Epoch: 90/800, loss: 67.22598990385825, correct: 59
Epoch: 100/800, loss: 67.16180934657395, correct: 59
Epoch: 110/800, loss: 67.1115768306706, correct: 59
Epoch: 120/800, loss: 67.07809724695242, correct: 59
Epoch: 130/800, loss: 67.11733012336356, correct: 58
Epoch: 140/800, loss: 67.91770004628565, correct: 56
Epoch: 150/800, loss: 67.75075790109916, correct: 57
Epoch: 160/800, loss: 67.02369834157997, correct: 59
Epoch: 170/800, loss: 66.90857207579833, correct: 60
Epoch: 180/800, loss: 66.85750751233614, correct: 61
Epoch: 190/800, loss: 66.82017906819246, correct: 62
Epoch: 200/800, loss: 66.78448772016571, correct: 61
Epoch: 210/800, loss: 66.76914997839802, correct: 61
Epoch: 220/800, loss: 66.81485487565084, correct: 59
Epoch: 230/800, loss: 67.1187002168632, correct: 59
Epoch: 240/800, loss: 67.4743444867311, correct: 58
Epoch: 250/800, loss: 66.86638568031049, correct: 59
Epoch: 260/800, loss: 66.65694324633758, correct: 61
Epoch: 270/800, loss: 66.59534121561506, correct: 61
Epoch: 280/800, loss: 66.54710901575048, correct: 62
Epoch: 290/800, loss: 66.48928704952958, correct: 63
Epoch: 300/800, loss: 66.44473076351856, correct: 63
Epoch: 310/800, loss: 66.42896690524198, correct: 63
Epoch: 320/800, loss: 66.56593390066378, correct: 60
Epoch: 330/800, loss: 67.55987440948081, correct: 57
Epoch: 340/800, loss: 67.00672246721416, correct: 59
Epoch: 350/800, loss: 66.38427251096014, correct: 62
Epoch: 360/800, loss: 66.2885792241174, correct: 65
Epoch: 370/800, loss: 66.23760566980627, correct: 65
Epoch: 380/800, loss: 66.22157577727768, correct: 64
Epoch: 390/800, loss: 66.25367782328853, correct: 63
Epoch: 400/800, loss: 66.52803458390036, correct: 60
Epoch: 410/800, loss: 66.9041016428288, correct: 59
Epoch: 420/800, loss: 66.5303692735563, correct: 60
Epoch: 430/800, loss: 66.16805390578745, correct: 63
Epoch: 440/800, loss: 66.03888145705572, correct: 64
Epoch: 450/800, loss: 66.03786669572139, correct: 64
Epoch: 460/800, loss: 66.35651281312289, correct: 60
Epoch: 470/800, loss: 66.58408191620555, correct: 58
Epoch: 480/800, loss: 66.28639014046112, correct: 59
Epoch: 490/800, loss: 66.07044609176802, correct: 61
Epoch: 500/800, loss: 66.16972409543986, correct: 61
Epoch: 510/800, loss: 66.41188363091103, correct: 58
Epoch: 520/800, loss: 66.21073204313929, correct: 59
Epoch: 530/800, loss: 66.01169334681082, correct: 62
Epoch: 540/800, loss: 66.01274434877672, correct: 62
Epoch: 550/800, loss: 66.13968554796033, correct: 59
Epoch: 560/800, loss: 66.19985098615524, correct: 59
Epoch: 570/800, loss: 66.00147190984971, correct: 59
Epoch: 580/800, loss: 65.71020712500398, correct: 64
Epoch: 590/800, loss: 65.69276038520641, correct: 63
Epoch: 600/800, loss: 66.04719656233772, correct: 60
Epoch: 610/800, loss: 66.42017604868686, correct: 59
Epoch: 620/800, loss: 65.77007218943562, correct: 61
Epoch: 630/800, loss: 65.31954692949326, correct: 65
Epoch: 640/800, loss: 65.35551104034107, correct: 64
Epoch: 650/800, loss: 65.67218462840162, correct: 60
Epoch: 660/800, loss: 66.29336312111269, correct: 57
Epoch: 670/800, loss: 65.64219436642684, correct: 60
Epoch: 680/800, loss: 64.96666297504355, correct: 65
Epoch: 690/800, loss: 64.79786552167211, correct: 65
Epoch: 700/800, loss: 66.81787222614338, correct: 55
Epoch: 710/800, loss: 66.1673478254152, correct: 54
Epoch: 720/800, loss: 64.87356254426247, correct: 65
Epoch: 730/800, loss: 65.28164531717466, correct: 60
Epoch: 740/800, loss: 65.1062740310185, correct: 61
Epoch: 750/800, loss: 64.84382020191603, correct: 56
Epoch: 760/800, loss: 65.31173827429417, correct: 55
Epoch: 770/800, loss: 65.13793115880473, correct: 55
Epoch: 780/800, loss: 65.30643390184454, correct: 56
Epoch: 790/800, loss: 64.88802310697932, correct: 55
Epoch: 800/800, loss: 65.05789666592386, correct: 56
```
