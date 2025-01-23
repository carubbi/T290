# Pacote `strings`

## Submódulos

### `strings.boyer_moore`
Classe `BoyerMoore`
- Implementa o algoritmo de busca Boyer-Moore (com a regra do caractere ruim).
  - **Método principal**: `search(txt)`: Retorna o índice da primeira ocorrência de um padrão em um texto ou `N` se não houver correspondência.

---

### `strings.huffman_compression`
- Métodos estáticos para compressão e expansão usando o código de Huffman.
  - **Compressão**: `compress()`.
  - **Expansão**: `expand()`.

---

### `strings.kmp`
Classe `KMP`
- Implementa o algoritmo de busca de padrão Knuth-Morris-Pratt.
  - **Método principal**: `search(txt)`: Retorna o índice da primeira ocorrência de um padrão em um texto ou `N` se não houver correspondência.

---

### `strings.lsd`
- Ordenação de strings usando o algoritmo LSD (Least Significant Digit).
  - **Função principal**: `sort(a, w, radix=256)`.

---

### `strings.lzw`
- Métodos estáticos para compressão e expansão usando o algoritmo LZW.
  - **Compressão**: `compress()`.
  - **Expansão**: `expand()`.

---

### `strings.msd`
- Ordenação de strings usando o algoritmo MSD (Most Significant Digit).
  - **Função principal**: `sort(a, radix=256)`.

---

### `strings.nfa`
Classe `NFA`
- Implementa um autômato finito não determinístico para correspondência com expressões regulares.
  - **Método principal**: `recognizes(txt)`: Retorna `True` se o texto corresponder à expressão regular.

---

### `strings.quick3string`
- Ordenação de strings usando o algoritmo QuickSort com particionamento de 3 vias.
  - **Função principal**: `sort(a)`.

---

### `strings.rabin_karp`
Classe `RabinKarp`
- Implementa o algoritmo de busca Rabin-Karp (versão Monte Carlo).
  - **Método principal**: `search(txt)`: Retorna o índice da primeira ocorrência de um padrão em um texto ou `N` se não houver correspondência.
  - **Função auxiliar**: `long_random_prime(k)`: Gera um número primo aleatório com `k` bits.

---

### `strings.trie_st`
Classe `TrieST`
- Implementa uma Trie para armazenar chaves e valores.
  - Operações: `put(key, val)`, `get(key)`, `delete(key)`, `keys()`, `keys_with_prefix(prefix)`.

---

### `strings.tst`
Classe `TST`
- Implementa uma TST (trie ternária de busca).
  - Operações: `put(key, val)`, `get(key)`, `keys()`, `keys_with_prefix(prefix)`.

---

# Fonte: 
- [Algorithms, 4th Edition.](https://algs4.cs.princeton.edu/home/)
- [Research group at ITU Copenhagen](https://itualgs4.readthedocs.io/en/latest/source/graphs.html)
- [Computer Science at Princeton University](https://www.cs.princeton.edu/courses/archive/fall20/cos226/syllabus.php)
