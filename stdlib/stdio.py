# code based on https://introcs.cs.princeton.edu/python/code/stdlib-python.zip as downloaded in dec 2017

"""stdio.py.

The stdio module supports reading from standard input and writing to
sys.stdout.

Note:  Usually it's a bad idea to mix these three sets of reading
functions:

-- isEmpty(), readInt(), readFloat(), readBool(), readString()

-- hasNextLine(), readLine()

-- readAll(), readAllInts(), readAllFloats(), readAllBools(),
   readAllStrings(), readAllLines()

Usually it's better to use one set exclusively.

"""

import re
import sys

# -----------------------------------------------------------------------

# Change sys.stdin so it provides universal newline support.

if sys.hexversion < 0x03000000:
    import os

    sys.stdin = os.fdopen(sys.stdin.fileno(), "rU", 0)
else:
    sys.stdin = open(sys.stdin.fileno(), "r", newline=None)

# =======================================================================
# print to stderr
# from https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python#14981125
# =======================================================================


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# =======================================================================
# Writing functions
# =======================================================================


def writeln(x=""):
    """Escreve x na saída padrão sem adicionar uma quebra de linha.

    :param x: O texto a ser escrito.
    """
    if sys.hexversion < 0x03000000:
        print("Error: Python 3 is required.", file=sys.stderr)
        sys.exit(1)
        # x = unicode(x)
        # x = x.encode("utf-8")
    else:
        x = str(x)
    
    sys.stdout.write(x)
    sys.stdout.write("\n")
    sys.stdout.flush()


# -----------------------------------------------------------------------


def write(x=""):
    """Escreve x na saída padrão sem adicionar uma quebra de linha.

    :param x: O texto a ser escrito.
    """
    if sys.hexversion < 0x03000000:
        print("Error: Python 3 is required.", file=sys.stderr)
        sys.exit(1)
        # x = unicode(x)
        # x = x.encode("utf-8")
    else:
        x = str(x)
    
    sys.stdout.write(x)
    sys.stdout.flush()


# -----------------------------------------------------------------------


def writef(fmt, *args):
    """Escreve x na saída padrão com um formato especificado.

    :param fmt: A string de formato.
    :param args: Os argumentos a serem formatados e escritos.
    """
    x = fmt % args
    if sys.hexversion < 0x03000000:
        print("Error: Python 3 is required.", file=sys.stderr)
        sys.exit(1)
        # x = unicode(x)
        # x = x.encode("utf-8")
    
    sys.stdout.write(x)
    sys.stdout.flush()


# =======================================================================
# Reading functions
# =======================================================================

_buffer = ""

# -----------------------------------------------------------------------


def _readRegExp(regExp):
    """Descarta os caracteres em branco iniciais da entrada padrão.

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
    """Retorna True se não restarem caracteres não em branco na entrada padrão.

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
    """Discard leading white space characters from standard input.

    Then read from standard input a sequence of characters comprising an
    integer. Convert the sequence of characters to an integer, and
    return the integer.  Raise an EOFError if no non-whitespace
    characters remain in standard input. Raise a ValueError if the next
    characters to be read from standard input cannot comprise an
    integer.

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
    """Read all remaining strings from standard input, convert each to an int,
    and return those ints in an array.

    Raise a ValueError if any of the strings cannot be converted to an
    int.

    """
    strings = readAllStrings()
    ints = []
    
    for s in strings:
        i = int(s)
        ints.append(i)
    
    return ints


# -----------------------------------------------------------------------


def readFloat():
    """Discard leading white space characters from standard input.

    Then read from standard input a sequence of characters comprising a
    float. Convert the sequence of characters to a float, and return the
    float.  Raise an EOFError if no non-whitespace characters remain in
    standard input. Raise a ValueError if the next characters to be read
    from standard input cannot comprise a float.

    """
    s = _readRegExp(r"[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?")
    
    return float(s)


# -----------------------------------------------------------------------


def readAllFloats():
    """Read all remaining strings from standard input, convert each to a float,
    and return those floats in an array.

    Raise a ValueError if any of the strings cannot be converted to a
    float.

    """
    strings = readAllStrings()
    floats = []
    
    for s in strings:
        f = float(s)
        floats.append(f)
    
    return floats


# -----------------------------------------------------------------------


def readBool():
    """Discard leading white space characters from standard input. Then read
    from standard input a sequence of characters comprising a bool. Convert the
    sequence of characters to a bool, and return the bool.  Raise an EOFError
    if no non-whitespace characters remain in standard input. Raise a
    ValueError if the next characters to be read from standard input cannot
    comprise a bool.

    These character sequences can comprise a bool:
    -- True
    -- False
    -- 1 (means true)
    -- 0 (means false)

    """
    s = _readRegExp(r"(True)|(False)|1|0")
    
    if (s == "True") or (s == "1"):
        return True
    
    return False


# -----------------------------------------------------------------------


def readAllBools():
    """Read all remaining strings from standard input, convert each to a bool,
    and return those bools in an array.

    Raise a ValueError if any of the strings cannot be converted to a
    bool.

    """
    strings = readAllStrings()
    bools = []
    
    for s in strings:
        b = bool(s)
        bools.append(b)
    
    return bools


# -----------------------------------------------------------------------


def readString():
    """Descarta os caracteres em branco iniciais da entrada padrão.

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
    """Read all remaining strings from standard input, and return them in an
    array."""
    
    strings = []

    while not isEmpty():
        s = readString()
        strings.append(s)
    
    return strings


# -----------------------------------------------------------------------


def hasNextLine():
    """Retorna True se houver uma próxima linha na entrada padrão.

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
    """Lê e retorna a próxima linha da entrada padrão como uma string.

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
    """Lê todas as linhas restantes da entrada padrão e retorna uma lista com elas.

    :returns: Lista de linhas lidas da entrada padrão.
    """
    lines = []
    
    while hasNextLine():
        line = readLine()
        lines.append(line)
    
    return lines


# -----------------------------------------------------------------------


def readAll():
    """Lê e retorna todo o conteúdo restante da entrada padrão como uma string.

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
# For Testing
# =======================================================================


def _testWrite():
    writeln()
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
    """For testing.

    The command-line argument should be the name of the function that
    should be called.

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
