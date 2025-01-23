# Pacote `itu.algs4.searching`

## Submódulos

### `itu.algs4.searching.binary_search_st`

#### Classe `BinarySearchST`

Representa uma tabela de símbolos ordenada para pares chave-valor genéricos.

##### Características:
- **Base:** `object`
- Implementação baseada em um array ordenado.
- Métodos suportados: inserção (`put`), busca (`get`), remoção (`delete`), ordenação (`ceiling`, `floor`, `select`) e iteração sobre chaves.

##### Métodos Principais:
- `ceiling(key)`: Retorna a menor chave maior ou igual a `key`.
- `delete(key)`: Remove uma chave e seu valor associado.
- `put(key, val)`: Insere ou atualiza um par chave-valor.
- `get(key)`: Retorna o valor associado a uma chave.
- `keys()`: Retorna todas as chaves como um Iterable.
- `size()`: Retorna o número de pares chave-valor.

---

### `itu.algs4.searching.bst`

#### Classe `BST`

Representa uma tabela de símbolos baseada em uma árvore de busca binária (BST).

##### Características:
- **Base:** `typing.Generic`
- Suporte a operações como inserção, busca, remoção e ordenação.
- Métodos adicionais para calcular altura e realizar ordenação por nível.

##### Métodos Principais:
- `put(key, value)`: Insere ou atualiza um par chave-valor.
- `get(key)`: Retorna o valor associado a uma chave.
- `delete(key)`: Remove uma chave e seu valor associado.
- `keys()`: Retorna todas as chaves na tabela de símbolos.
- `height()`: Calcula a altura da árvore.

---

### `itu.algs4.searching.linear_probing_hst`

#### Classe `LinearProbingHashST`

Tabela de símbolos baseada em hashing com sondagem linear.

##### Características:
- **Base:** `object`
- Operações de inserção, busca e remoção em tempo constante esperado.

##### Métodos Principais:
- `put(key, value)`: Insere ou atualiza um par chave-valor.
- `get(key)`: Retorna o valor associado a uma chave.
- `delete(key)`: Remove uma chave e seu valor associado.
- `key_list()`: Retorna todas as chaves como uma lista.
- `size()`: Retorna o número de pares chave-valor.

---

### `itu.algs4.searching.red_black_bst`

#### Classe `RedBlackBST`

Tabela de símbolos baseada em uma árvore rubro-negra balanceada.

##### Características:
- **Base:** `typing.Generic`
- Operações como inserção e remoção possuem tempo logarítmico no pior caso.

##### Métodos Principais:
- `put(key, val)`: Insere ou atualiza um par chave-valor.
- `delete(key)`: Remove uma chave e seu valor associado.
- `keys()`: Retorna todas as chaves na tabela de símbolos.
- `height()`: Retorna a altura da árvore.
- `size()`: Retorna o número de pares chave-valor.

---

### `itu.algs4.searching.seperate_chaining_hst`

#### Classe `SeparateChainingHashST`

Tabela de símbolos baseada em hashing com encadeamento separado.

##### Características:
- **Base:** `object`
- Alta eficiência para inserção e busca, com tempo constante esperado.

##### Métodos Principais:
- `put(key, value)`: Insere ou atualiza um par chave-valor.
- `get(key)`: Retorna o valor associado a uma chave.
- `delete(key)`: Remove uma chave e seu valor associado.
- `keys()`: Retorna todas as chaves como um Iterable.
- `size()`: Retorna o número de pares chave-valor.

---

### `itu.algs4.searching.sparse_vector`

#### Classe `SparseVector`

Representa um vetor matemático esparso com operações para soma, produto interno, e escala.

##### Características:
- **Base:** `object`
- Representação eficiente de vetores com muitos valores zero.

##### Métodos Principais:
- `put(i, value)`: Define o valor de um índice.
- `get(i)`: Retorna o valor em um índice.
- `magnitude()`: Calcula a magnitude do vetor.
- `plus(that)`: Soma dois vetores esparsos.
- `dot(that)`: Calcula o produto interno.

---

### `itu.algs4.searching.st`

#### Classe `ST`

Representa uma tabela de símbolos genérica com métodos básicos para operações chave-valor.

##### Métodos Principais:
- `put(key, val)`: Insere ou atualiza um par chave-valor.
- `get(key)`: Retorna o valor associado a uma chave.
- `delete(key)`: Remove uma chave e seu valor associado.
- `keys()`: Retorna todas as chaves na tabela de símbolos.

---

# Fonte: 
- [Algorithms, 4th Edition.](https://algs4.cs.princeton.edu/home/)
- [Research group at ITU Copenhagen](https://itualgs4.readthedocs.io/en/latest/source/itu.algs4.graphs.html)
- [Computer Science at Princeton University](https://www.cs.princeton.edu/courses/archive/fall20/cos226/syllabus.php)