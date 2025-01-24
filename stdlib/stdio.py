import re
import sys

# -----------------------------------------------------------------------
# Ajusta sys.stdin para suportar newlines universais.
if sys.hexversion < 0x03000000:
    import os

    # Substitui sys.stdin para suportar quebras de linha universais no Python 2.
    sys.stdin = os.fdopen(sys.stdin.fileno(), "rU", 0)
else:
    # Substitui sys.stdin para suportar quebras de linha universais no Python 3.
    sys.stdin = open(sys.stdin.fileno(), "r", newline=None)

# =======================================================================
# Função para imprimir mensagens em stderr.
# Baseado em: https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python#14981125
# =======================================================================

def eprint(*args, **kwargs):
    """
    Imprime mensagens no fluxo de erro padrão (stderr).

    :param args: Argumentos posicionais para a função print.
    :param kwargs: Argumentos nomeados para a função print.
    :returns: None
    """
    print(*args, file=sys.stderr, **kwargs)

# =======================================================================
# Funções para escrita na saída padrão.
# =======================================================================

def writeln(x=""):
    """
    Escreve x na saída padrão seguido por uma quebra de linha.

    :param x: O texto a ser escrito.
    :returns: None
    """
    if sys.hexversion < 0x03000000:
        print("Error: Python 3 is required.", file=sys.stderr)
        sys.exit(1)
    else:
        x = str(x)

    sys.stdout.write(x)
    sys.stdout.write("\n")
    sys.stdout.flush()

# -----------------------------------------------------------------------

def write(x=""):
    """
    Escreve x na saída padrão sem adicionar uma quebra de linha.

    :param x: O texto a ser escrito.
    :returns: None
    """
    if sys.hexversion < 0x03000000:
        print("Error: Python 3 is required.", file=sys.stderr)
        sys.exit(1)
    else:
        x = str(x)

    sys.stdout.write(x)
    sys.stdout.flush()

# -----------------------------------------------------------------------

def writef(fmt, *args):
    """
    Escreve na saída padrão com um formato especificado.

    :param fmt: A string de formato.
    :param args: Os argumentos a serem formatados e escritos.
    :returns: None
    """
    x = fmt % args
    if sys.hexversion < 0x03000000:
        print("Error: Python 3 is required.", file=sys.stderr)
        sys.exit(1)

    sys.stdout.write(x)
    sys.stdout.flush()

# =======================================================================
# Funções para leitura da entrada padrão.
# =======================================================================

_buffer = ""

# -----------------------------------------------------------------------

def _readRegExp(regExp):
    """
    Descarta os caracteres em branco iniciais da entrada padrão.

    Em seguida, lê da entrada padrão e retorna uma string que corresponde
    à expressão regular regExp. Levanta um EOFError se não restarem
    caracteres não em branco na entrada padrão. Levanta um ValueError se
    os próximos caracteres a serem lidos da entrada padrão não corresponderem
    a 'regExp'.

    :param regExp: Expressão regular que define o padrão a ser lido.
    :returns: String que corresponde ao padrão especificado.
    :raises EOFError: Se a entrada padrão estiver vazia.
    :raises ValueError: Se os caracteres não corresponderem ao padrão.
    """
    global _buffer

    if isEmpty():
        raise EOFError()

    compiledRegExp = re.compile(r"^\s*" + regExp)
    match = compiledRegExp.search(_buffer)

    if match is None:
        raise ValueError()

    s = match.group()
    _buffer = _buffer[match.end() :]

    return s.lstrip()

# -----------------------------------------------------------------------

def isEmpty():
    """
    Retorna True se não restarem caracteres não em branco na entrada padrão.

    Caso contrário, retorna False.

    :returns: True se a entrada estiver vazia, False caso contrário.
    """
    global _buffer

    while _buffer.strip() == "":
        line = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            line = line.decode("utf-8")
        if line == "":
            return True
        _buffer += line

    return False

# -----------------------------------------------------------------------

def readInt():
    """
    Lê um inteiro da entrada padrão.

    Descarta caracteres em branco iniciais e converte a sequência de
    caracteres em um inteiro. Levanta EOFError se não houver caracteres
    não em branco e ValueError se a sequência não for um inteiro válido.

    :returns: O inteiro lido da entrada.
    :raises EOFError: Se a entrada estiver vazia.
    :raises ValueError: Se os caracteres não puderem ser convertidos.
    """
    s = _readRegExp(r"[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)")
    radix = 10
    strLength = len(s)

    if (strLength >= 1) and (s[0:1] == "0"):
        radix = 8
    if (strLength >= 2) and (s[0:2] == "-0"):
        radix = 8
    if (strLength >= 2) and (s[0:2] == "0x"):
        radix = 16
    if (strLength >= 2) and (s[0:2] == "0X"):
        radix = 16
    if (strLength >= 3) and (s[0:3] == "-0x"):
        radix = 16
    if (strLength >= 3) and (s[0:3] == "-0X"):
        radix = 16

    return int(s, radix)

# -----------------------------------------------------------------------

def readAllInts():
    """
    Lê todos os inteiros restantes da entrada padrão e os retorna como uma lista.

    Levanta ValueError se algum dos valores não puder ser convertido.

    :returns: Lista de inteiros lidos da entrada.
    """
    strings = readAllStrings()
    ints = []

    for s in strings:
        i = int(s)
        ints.append(i)

    return ints

# -----------------------------------------------------------------------

def readFloat():
    """
    Lê um número em ponto flutuante da entrada padrão.

    Descarta caracteres em branco iniciais e converte a sequência de
    caracteres em um float. Levanta EOFError se não houver caracteres
    não em branco e ValueError se a sequência não for um float válido.

    :returns: O float lido da entrada.
    :raises EOFError: Se a entrada estiver vazia.
    :raises ValueError: Se os caracteres não puderem ser convertidos.
    """
    s = _readRegExp(r"[-+]?\d*(\.\d+)?([eE][-+]?\d+)?")
    return float(s)

# -----------------------------------------------------------------------

def readAllFloats():
    """
    Lê todos os números em ponto flutuante restantes da entrada padrão e os retorna como uma lista.

    Levanta ValueError se algum dos valores não puder ser convertido.

    :returns: Lista de floats lidos da entrada.
    """
    strings = readAllStrings()
    floats = []

    for s in strings:
        f = float(s)
        floats.append(f)

    return floats

# -----------------------------------------------------------------------

def readBool():
    """
    Lê um valor booleano da entrada padrão.

    Descarta os caracteres em branco iniciais e converte a sequência de
    caracteres em um bool. Levanta EOFError se não houver caracteres
    não em branco e ValueError se a sequência não for um bool válido.

    Estes valores podem ser convertidos para bool:
    -- True
    -- False
    -- 1 (equivalente a True)
    -- 0 (equivalente a False)

    :returns: O valor booleano lido da entrada.
    :raises EOFError: Se a entrada estiver vazia.
    :raises ValueError: Se os caracteres não puderem ser convertidos.
    """
    s = _readRegExp(r"(True)|(False)|1|0")

    if (s == "True") or (s == "1"):
        return True

    return False

# -----------------------------------------------------------------------

def readAllBools():
    """
    Lê todos os valores booleanos restantes da entrada padrão e os retorna como uma lista.

    Levanta ValueError se algum dos valores não puder ser convertido.

    :returns: Lista de booleanos lidos da entrada.
    """
    strings = readAllStrings()
    bools = []

    for s in strings:
        if s in ["True", "1"]:
            bools.append(True)
        elif s in ["False", "0"]:
            bools.append(False)
        else:
            raise ValueError(f"Valor inválido para booleano: {s}")

    return bools

# -----------------------------------------------------------------------

def readString():
    """
    Descarta os caracteres em branco iniciais da entrada padrão.

    Em seguida, lê da entrada padrão uma sequência de caracteres que compõem
    uma string e retorna a string. Levanta um EOFError se não restarem
    caracteres não em branco na entrada padrão.

    :returns: A próxima string da entrada.
    :raises EOFError: Se a entrada padrão estiver vazia.
    """
    s = _readRegExp(r"\S+")
    return s

# -----------------------------------------------------------------------

def readAllStrings():
    """
    Lê todas as strings restantes da entrada padrão e as retorna como uma lista.

    :returns: Lista de strings lidas da entrada.
    """
    strings = []

    while not isEmpty():
        s = readString()
        strings.append(s)

    return strings

# -----------------------------------------------------------------------

def hasNextLine():
    """
    Retorna True se houver uma próxima linha na entrada padrão.

    Caso contrário, retorna False.

    :returns: True se houver uma próxima linha, False caso contrário.
    """
    global _buffer

    if _buffer != "":
        return True
    else:
        _buffer = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            _buffer = _buffer.decode("utf-8")
        if _buffer == "":
            return False
        return True

# -----------------------------------------------------------------------

def readLine():
    """
    Lê e retorna a próxima linha da entrada padrão como uma string.

    Levanta um EOFError se não houver próxima linha.

    :returns: A próxima linha da entrada padrão.
    :raises EOFError: Se não houver próxima linha.
    """
    global _buffer

    if not hasNextLine():
        raise EOFError()
    s = _buffer
    _buffer = ""

    return s.rstrip("\n")

# -----------------------------------------------------------------------

def readAllLines():
    """
    Lê todas as linhas restantes da entrada padrão e retorna uma lista com elas.

    :returns: Lista de linhas lidas da entrada padrão.
    """
    lines = []

    while hasNextLine():
        line = readLine()
        lines.append(line)

    return lines

# -----------------------------------------------------------------------

def readAll():
    """
    Lê e retorna todo o conteúdo restante da entrada padrão como uma string.

    :returns: Todo o conteúdo restante da entrada padrão.
    """
    global _buffer

    s = _buffer
    _buffer = ""

    for line in sys.stdin:
        if sys.hexversion < 0x03000000:
            line = line.decode("utf-8")
        s += line

    return s

# =======================================================================
# Funções de teste.
# =======================================================================

def _testWrite():
    """
    Testa as funções de escrita.

    Chama funções write, writeln e writef com diferentes entradas para validação.

    :returns: None
    """
    writeln("string")
    writeln(123456)
    writeln(123.456)
    writeln(True)
    write()
    write("string")
    write(123456)
    write(123.456)
    write(True)
    writeln()
    writef("<%s> <%8d> <%14.8f>\n", "string", 123456, 123.456)
    writef("formatstring\n")

# -----------------------------------------------------------------------

def _main():
    """
    Função principal para teste.

    O argumento da linha de comando deve ser o nome da função que será chamada.

    :returns: None
    """
    map = {
        "readInt": readInt,
        "readAllInts": readAllInts,
        "readFloat": readFloat,
        "readAllFloats": readAllFloats,
        "readBool": readBool,
        "readAllBools": readAllBools,
        "readString": readString,
        "readAllStrings": readAllStrings,
        "readLine": readLine,
        "readAllLines": readAllLines,
        "readAll": readAll,
    }

    testId = sys.argv[1]

    if testId == "write":
        _testWrite()
    else:
        writeln(map[testId]())

if __name__ == "__main__":
    _main()