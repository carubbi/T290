# Pacote `sorting`

## Submódulos

### `sorting.heap`

#### Métodos Principais:
- `sort(pq)`: Reordena o array em ordem ascendente usando ordenação por heapsort.
- `main()`: Lê uma sequência de strings, aplica heapsort e imprime o resultado.

---

### `sorting.index_min_pq`

#### Classe `IndexMinPQ`
Implementa uma fila de prioridade indexada com chaves genéricas.

##### Métodos:
- `insert(i, key)`: Associa uma chave ao índice `i`.
- `del_min()`: Remove e retorna o índice da menor chave.
- `change_key(i, key)`: Altera a chave associada ao índice `i`.
- `min_key()`: Retorna a menor chave.
- `min_index()`: Retorna o índice da menor chave.
- `size()`: Retorna o número de itens na fila de prioridade.
- `is_empty()`: Verifica se a fila está vazia.

---

### `sorting.insertion_sort`

#### Métodos Principais:
- `sort(a)`: Ordena um array em ordem crescente utilizando o método de inserção.
- `is_sorted(a)`: Verifica se o array está ordenado.
- `main()`: Lê strings, aplica o algoritmo de inserção e imprime o resultado.

---

### `sorting.max_pq`

#### Classe `MaxPQ`
Fila de prioridade máxima baseada em heap binário.

##### Métodos:
- `insert(x)`: Insere uma nova chave.
- `del_max()`: Remove e retorna a maior chave.
- `max()`: Retorna a maior chave.
- `size()`: Retorna o número de elementos na fila.
- `is_empty()`: Verifica se a fila está vazia.

---

### `sorting.min_pq`

#### Classe `MinPQ`
Fila de prioridade mínima baseada em heap binário.

##### Métodos:
- `insert(x)`: Insere uma nova chave.
- `del_min()`: Remove e retorna a menor chave.
- `min()`: Retorna a menor chave.
- `size()`: Retorna o número de elementos na fila.
- `is_empty()`: Verifica se a fila está vazia.

---

### `sorting.merge`

#### Métodos:
- `sort(a)`: Ordena o array em ordem crescente usando mergesort.

---

### `sorting.merge_bu`

#### Métodos:
- `sort(a)`: Ordena o array utilizando mergesort bottom-up.

---

### `sorting.quick3way`

#### Métodos:
- `sort(a)`: Ordena um array em ordem crescente usando quicksort com partição 3-way.
- `is_sorted(a)`: Verifica se o array está ordenado.

---

### `sorting.quicksort`

#### Métodos:
- `sort(array)`: Ordena um array em ordem crescente usando quicksort.
- `select(array, k)`: Reorganiza o array para que o k-ésimo menor elemento esteja em `array[k]`.
- `is_sorted(array)`: Verifica se o array está ordenado.

---

### `sorting.selection`

#### Métodos:
- `sort(a)`: Ordena um array usando o método de seleção.
- `main()`: Lê strings, ordena e imprime os resultados.

---

### `sorting.shellsort`

#### Métodos:
- `sort(a)`: Ordena um array usando o algoritmo de shellsort.
- `is_sorted(a)`: Verifica se o array está ordenado.
- `main()`: Lê strings, aplica shellsort e imprime os resultados.

---

# Fonte: 
- [Algorithms, 4th Edition.](https://algs4.cs.princeton.edu/home/)
- [Research group at ITU Copenhagen](https://itualgs4.readthedocs.io/en/latest/source/graphs.html)
- [Computer Science at Princeton University](https://www.cs.princeton.edu/courses/archive/fall20/cos226/syllabus.php)
