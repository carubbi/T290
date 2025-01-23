# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""stdarray.py.

O módulo stdarray define funções relacionadas à criação, leitura e
escrita de arrays unidimensionais e bidimensionais.

"""

from stdio import writeln, write, readInt, readFloat, readBool

# =======================================================================
# Funções para criação de arrays
# =======================================================================


def create1D(length, value=None):
    """Cria e retorna um array unidimensional contendo "length" elementos,
    cada um inicializado para "value".

    :param length: Comprimento do array.
    :param value: Valor inicial de cada elemento (opcional).
    :returns: Array unidimensional.
    """
    return [value] * length


# -----------------------------------------------------------------------

def create2D(rowCount, colCount, value=None):
    """Cria e retorna um array bidimensional com "rowCount" linhas e
    "colCount" colunas, com cada elemento inicializado para "value".

    :param rowCount: Número de linhas.
    :param colCount: Número de colunas.
    :param value: Valor inicial de cada elemento (opcional).
    :returns: Array bidimensional.
    """
    a = [None] * rowCount
    for row in range(rowCount):
        a[row] = [value] * colCount
    return a


# =======================================================================
# Funções para escrita de arrays
# =======================================================================


def write1D(a):
    """Escreve o array unidimensional "a" para sys.stdout.

    Primeiro escreve o comprimento do array. Objetos booleanos são
    escritos como 0 e 1, não como False e True.

    :param a: Array unidimensional a ser escrito.
    """
    length = len(a)
    writeln(length)  # Escreve o comprimento do array

    for i in range(length):
        element = a[i]
        if isinstance(element, bool):
            write(1 if element else 0)  # Escreve 1 ou 0 para booleanos
        else:
            write(element)
        write(" ")  # Adiciona espaço entre elementos

    writeln()  # Nova linha após o array


# -----------------------------------------------------------------------

def write2D(a):
    """Escreve o array bidimensional "a" para sys.stdout.

    Primeiro escreve suas dimensões. Objetos booleanos são
    escritos como 0 e 1, não como False e True.

    :param a: Array bidimensional a ser escrito.
    """
    rowCount = len(a)
    colCount = len(a[0])
    writeln(f"{rowCount} {colCount}")  # Escreve dimensões do array

    for row in range(rowCount):
        for col in range(colCount):
            element = a[row][col]
            if isinstance(element, bool):
                write(1 if element else 0)  # Escreve 1 ou 0 para booleanos
            else:
                write(element)
            write(" ")  # Adiciona espaço entre elementos

        writeln()  # Nova linha após cada linha do array


# =======================================================================
# Funções para leitura de arrays
# =======================================================================


def readInt1D():
    """Lê de sys.stdin e retorna um array de inteiros.

    Um inteiro no início de sys.stdin define o comprimento do array.

    :returns: Array unidimensional de inteiros.
    """
    count = readInt()
    a = create1D(count, None)
    for i in range(count):
        a[i] = readInt()
    return a


# -----------------------------------------------------------------------

def readInt2D():
    """Lê de sys.stdin e retorna um array bidimensional de inteiros.

    Dois inteiros no início de sys.stdin definem as dimensões do array.

    :returns: Array bidimensional de inteiros.
    """
    rowCount = readInt()
    colCount = readInt()
    a = create2D(rowCount, colCount, 0)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = readInt()
    return a


# -----------------------------------------------------------------------

def readFloat1D():
    """Lê de sys.stdin e retorna um array de floats.

    Um inteiro no início de sys.stdin define o comprimento do array.

    :returns: Array unidimensional de floats.
    """
    count = readInt()
    a = create1D(count, None)
    for i in range(count):
        a[i] = readFloat()
    return a


# -----------------------------------------------------------------------

def readFloat2D():
    """Lê de sys.stdin e retorna um array bidimensional de floats.

    Dois inteiros no início de sys.stdin definem as dimensões do array.

    :returns: Array bidimensional de floats.
    """
    rowCount = readInt()
    colCount = readInt()
    a = create2D(rowCount, colCount, 0.0)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = readFloat()
    return a


# -----------------------------------------------------------------------

def readBool1D():
    """Lê de sys.stdin e retorna um array de booleanos.

    Um inteiro no início de sys.stdin define o comprimento do array.

    :returns: Array unidimensional de booleanos.
    """
    count = readInt()
    a = create1D(count, None)
    for i in range(count):
        a[i] = readBool()
    return a


# -----------------------------------------------------------------------

def readBool2D():
    """Lê de sys.stdin e retorna um array bidimensional de booleanos.

    Dois inteiros no início de sys.stdin definem as dimensões do array.

    :returns: Array bidimensional de booleanos.
    """
    rowCount = readInt()
    colCount = readInt()
    a = create2D(rowCount, colCount, False)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = readBool()
    return a


# =======================================================================
# Função principal para testes
# =======================================================================

def main():
    """Executa testes para as funções do módulo stdarray.

    Lê arrays de sys.stdin e os escreve em sys.stdout.
    """
    writeln("Testando leitura e escrita de arrays bidimensionais de float:")
    write2D(readFloat2D())

    writeln("\nTestando leitura e escrita de arrays bidimensionais de booleanos:")
    write2D(readBool2D())


if __name__ == "__main__":
    main()