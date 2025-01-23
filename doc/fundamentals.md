# Módulo fundamentals.bag

## Classe `fundamentals.bag.Bag`

A classe `Bag` representa um saco (ou multiconjunto) de itens genéricos. Ela suporta operações de inserção e iteração sobre os itens em ordem arbitrária.

- **Base:** `typing.Generic`
- Implementação utiliza uma lista ligada simples com uma classe aninhada estática `Node`.

### Métodos
- `add(item: T) → None`: Adiciona o item ao saco.
  - **Parâmetros:** `item` – o item a ser adicionado.
- `is_empty() → bool`: Retorna `True` se o saco estiver vazio.
- `size() → int`: Retorna o número de itens no saco.

---

# Módulo fundamentals.binary_search

Fornece um método para busca binária de um item em um array ordenado.

### Métodos
- `index_of(a: List[T], key: T)`: Retorna o índice da chave especificada no array ordenado.
  - **Parâmetros:** 
    - `a` – array de itens (ordenado em ordem crescente).
    - `key` – chave a ser buscada.
  - **Retorno:** Índice da chave se presente, ou `-1` caso contrário.
- `main()`: Lê strings de dois arquivos, ordena o primeiro e imprime strings do segundo que não estão no primeiro.

---

# Módulo fundamentals.queue

## Classe `fundamentals.queue.Queue`

Representa uma fila (FIFO) de itens genéricos.

- **Base:** `typing.Generic`
- Implementação com lista ligada simples.

### Métodos
- `enqueue(item: T) → None`: Adiciona um item à fila.
- `dequeue() → T`: Remove e retorna o item mais antigo.
- `is_empty() → bool`: Retorna `True` se a fila estiver vazia.
- `peek() → T`: Retorna o item mais antigo sem removê-lo.
- `size() → int`: Retorna o número de itens na fila.

---

# Módulo fundamentals.stack

## Classe `fundamentals.stack.Stack`

Representa uma pilha (LIFO) de itens genéricos.

- **Base:** `typing.Generic`
- Implementação com lista ligada simples.

### Métodos
- `push(item: T) → None`: Adiciona um item à pilha.
- `pop() → T`: Remove e retorna o item mais recente.
- `peek() → T`: Retorna o item mais recente sem removê-lo.
- `is_empty() → bool`: Retorna `True` se a pilha estiver vazia.
- `size() → int`: Retorna o número de itens na pilha.

---

# Módulo fundamentals.uf

Implementa diferentes versões da estrutura de dados union-find (também conhecida como conjuntos disjuntos).

### Relação "conectado a" deve ser uma relação de equivalência:
- Reflexiva: `p` está conectado a `p`.
- Simétrica: Se `p` está conectado a `q`, então `q` está conectado a `p`.
- Transitiva: Se `p` está conectado a `q` e `q` está conectado a `r`, então `p` está conectado a `r`.

## Implementações

### Classe `QuickFindUF(n: int)`
- **Base:** `object`
- Implementação de Quick Find.
- Operações:
  - `connected(p: int, q: int) → bool`: Retorna `True` se `p` e `q` estão no mesmo componente.
  - `find(p: int) → int`: Retorna o identificador do componente de `p`.
  - `union(p: int, q: int) → None`: Une os componentes de `p` e `q`.

### Classe `QuickUnionUF(n: int)`
- **Base:** `object`
- Implementação de Quick Union.
- Operações idênticas ao QuickFindUF.

### Classe `UF(n: int)`
- **Base:** `object`
- Implementação com união ponderada por rank e compressão de caminho.
- Complexidade:
  - Operações `union`, `find` e `connected` têm tempo logarítmico no pior caso.

### Classe `WeightedQuickUnionUF(n: int)`
- **Base:** `object`
- Implementação com união ponderada por tamanho.
- Operações idênticas à classe `UF`.

---

# Outros Módulos e Métodos

## Binary Search
- Fornece busca binária em arrays ordenados.

## Métodos Auxiliares
- `java_string_hash(key)`: Calcula o código de hash de uma string no estilo Java.
- `trailing_zeros(i)`: Calcula o número de zeros à direita em um número binário.

## Métodos de Somas
- `ThreeSum`, `ThreeSumFast`, `TwoSumFast`: Classes para cálculos eficientes de somas de pares ou trios em arrays.

---

# Fonte: 
- [Algorithms, 4th Edition.](https://algs4.cs.princeton.edu/home/)
- [Research group at ITU Copenhagen](https://itualgs4.readthedocs.io/en/latest/source/itu.algs4.graphs.html)
- [Computer Science at Princeton University](https://www.cs.princeton.edu/courses/archive/fall20/cos226/syllabus.php)