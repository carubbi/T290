# Pacote `stdlib`

## Submódulos

### `stdlib.binary_out`
Classe `BinaryOut`
- Fornece métodos para manipulação binária de saída:
  - `write_bool(x)`: Escreve um valor booleano.
  - `write_byte(x)`: Escreve um byte.
  - `write_char(x)`: Escreve um caractere.
  - `write_int(x)`: Escreve um inteiro.
  - `write_string(s)`: Escreve uma string.

---

### `stdlib.binary_stdin`
Classe `BinaryStdIn`
- Permite manipulação binária de entrada:
  - `read_bool()`, `read_char()`, `read_int()`, `read_string()`: Lê diferentes tipos de dados binários.
  - `is_empty()`: Verifica se a entrada está vazia.

---

### `stdlib.binary_stdout`
Classe `BinaryStdOut`
- Permite manipulação binária de saída:
  - Métodos semelhantes a `BinaryOut`.

---

### `stdlib.color`
Classe `Color`
- Representa cores no modelo RGB:
  - `getRed()`, `getGreen()`, `getBlue()`: Retornam os componentes de cor.

---

### `stdlib.instream`
Classe `InStream`
- Manipulação de entrada de fluxo de texto:
  - Métodos para leitura:
    - `readInt()`, `readFloat()`, `readBool()`, `readString()`.
    - `readAll()`, `readAllLines()`, `readAllInts()`, etc.
  - Métodos para verificar status:
    - `isEmpty()`, `hasNextLine()`.

---

### `stdlib.outstream`
Classe `OutStream`
- Manipulação de saída de fluxo de texto:
  - Métodos para escrita:
    - `write(x)`, `writeln(x)`, `writef(fmt, *args)`.

---

### `stdlib.picture`
Classe `Picture`
- Modela uma imagem:
  - `width()`, `height()`: Retornam dimensões.
  - `get(x, y)`, `set(x, y, c)`: Manipulam pixels.
  - `save(f)`: Salva a imagem.

---

### `stdlib.stdarray`
Funções para criação e manipulação de arrays:
- Criação:
  - `create1D(length, value=None)`, `create2D(rowCount, colCount, value=None)`.
- Leitura:
  - `readInt1D()`, `readInt2D()`, `readFloat1D()`, etc.
- Escrita:
  - `write1D(a)`, `write2D(a)`.

---

### `stdlib.stddraw`
Funções para desenhos gráficos:
- Desenho de formas:
  - `circle()`, `filledRectangle()`, `polygon()`, etc.
- Configuração:
  - `setCanvasSize()`, `setPenColor()`, `setFontSize()`, etc.

---

### `stdlib.stdio`
Funções para entrada/saída padrão:
- Leitura:
  - `readInt()`, `readFloat()`, `readString()`, etc.
- Escrita:
  - `write()`, `writeln()`, `writef(fmt, *args)`.

---

### `stdlib.stdrandom`
Funções relacionadas a números pseudoaleatórios:
- Geração:
  - `uniformInt(lo, hi)`, `uniformFloat(lo, hi)`, `bernoulli(p)`, etc.
- Distribuições:
  - `gaussian(mean, stddev)`, `binomial(n, p)`, `exp(lambd)`.

---

### `stdlib.stdstats`
Funções para análise estatística:
- Cálculos:
  - `mean(a)`, `median(a)`, `stddev(a)`, `var(a)`.
- Gráficos:
  - `plotBars(a)`, `plotPoints(a)`, `plotLines(a)`.

---

# Fonte: 
- [Algorithms, 4th Edition.](https://algs4.cs.princeton.edu/home/)
- [Research group at ITU Copenhagen](https://itualgs4.readthedocs.io/en/latest/source/graphs.html)
- [Computer Science at Princeton University](https://www.cs.princeton.edu/courses/archive/fall20/cos226/syllabus.php)
