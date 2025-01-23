# Pacote `graphs`

## Submódulos

### `graphs.Arbitrage`
Módulo relacionado a arbitragem. Consulte a documentação para mais detalhes.

---

### `graphs.CPM`
Módulo para análise do Método do Caminho Crítico (Critical Path Method - CPM).

---

### `graphs.acyclic_lp`

#### Classe `graphs.acyclic_lp.AcyclicLP`

Representa um tipo de dado para resolver o problema de caminhos mais longos de uma única origem em grafos dirigidos acíclicos ponderados. 

- **Base:** `object`
- Suporta pesos de arestas positivos, negativos ou nulos.
- Algoritmo baseado em ordenação topológica.

##### Métodos
- `dist_to(v)`: Retorna o comprimento do caminho mais longo do vértice de origem `s` até o vértice `v`.
- `has_path_to(v)`: Verifica se existe um caminho do vértice de origem `s` até o vértice `v`.
- `path_to(v)`: Retorna o caminho mais longo do vértice de origem `s` até o vértice `v`.

---

### `graphs.acyclic_sp`

#### Classe `graphs.acyclic_sp.AcyclicSP`

Resolve o problema de caminhos mais curtos de uma única origem em grafos dirigidos acíclicos ponderados.

- **Base:** `object`
- Pesos de arestas podem ser positivos, negativos ou nulos.

##### Métodos
- `dist_to(v)`: Retorna o comprimento do caminho mais curto do vértice de origem `s` até `v`.
- `has_path_to(v)`: Verifica se há caminho de `s` até `v`.
- `path_to(v)`: Retorna o caminho mais curto de `s` até `v`.

---

### `graphs.bellman_ford_sp`

#### Classe `graphs.bellman_ford_sp.BellmanFordSP`

Resolve problemas de caminhos mais curtos usando o algoritmo de Bellman-Ford.

##### Métodos
- `dist_to(v)`: Retorna a distância para o vértice `v`.
- `has_negative_cycle()`: Verifica se há ciclos negativos.
- `has_path_to(v)`: Verifica se há um caminho até `v`.
- `path_to(v)`: Retorna o caminho até `v`.

---

### `graphs.bipartite`

#### Classe `graphs.bipartite.Bipartite`

Determina se um grafo não dirigido é bipartido ou possui ciclos de comprimento ímpar.

##### Métodos
- `is_bipartite()`: Verifica se o grafo é bipartido.
- `color(v)`: Retorna o lado do bipartido onde o vértice `v` está localizado.
- `odd_cycle()`: Retorna um ciclo de comprimento ímpar, caso o grafo não seja bipartido.

---

### `graphs.breadth_first_paths`

#### Classe `graphs.breadth_first_paths.BreadthFirstPaths`

Encontra caminhos mais curtos (em número de arestas) a partir de um vértice de origem para todos os outros vértices em um grafo.

##### Métodos
- `dist_to(v)`: Retorna o número de arestas no caminho mais curto até `v`.
- `has_path_to(v)`: Verifica se existe caminho até `v`.
- `path_to(v)`: Retorna o caminho mais curto até `v`.

---

### `graphs.cc`

#### Classe `graphs.cc.CC`

Determina os componentes conectados em um grafo não dirigido.

##### Métodos
- `connected(v, w)`: Verifica se os vértices `v` e `w` pertencem ao mesmo componente conectado.
- `count()`: Retorna o número de componentes conectados.
- `id(v)`: Retorna o identificador do componente conectado que contém `v`.

---

### `graphs.cycle`

#### Classe `graphs.cycle.Cycle`

Determina se um grafo não dirigido contém um ciclo.

##### Métodos
- `has_cycle()`: Verifica se o grafo contém ciclos.
- `cycle()`: Retorna um ciclo no grafo, caso exista.

---

### `graphs.degrees_of_separation`

#### Classe `graphs.degrees_of_separation.DegreesOfSeparation`

Calcula o grau de separação entre indivíduos em uma rede social. Exemplo: calcular o número de Bacon de Kevin Bacon em uma rede de filmes.

---

### `graphs.depth_first_order`

#### Classe `graphs.depth_first_order.DepthFirstOrder`

Determina ordens de busca em profundidade (pré-ordem, pós-ordem e pós-ordem reversa) em um grafo dirigido.

##### Métodos
- `pre(v)`: Retorna a pré-ordem do vértice `v`.
- `post(v)`: Retorna a pós-ordem do vértice `v`.
- `reverse_post()`: Retorna a pós-ordem reversa.

---

# Fonte: 
- [Algorithms, 4th Edition.](https://algs4.cs.princeton.edu/home/)
- [Research group at ITU Copenhagen](https://itualgs4.readthedocs.io/en/latest/source/graphs.html)
- [Computer Science at Princeton University](https://www.cs.princeton.edu/courses/archive/fall20/cos226/syllabus.php)