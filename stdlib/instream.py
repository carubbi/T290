# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""instream.py.

O módulo instream define a classe InStream.

"""

# -----------------------------------------------------------------------

import re
import sys

if sys.hexversion < 0x03000000:
    import urllib
else:
    from urllib import request as urllib

# -----------------------------------------------------------------------


class InStream:
    """Um objeto InStream encapsula um arquivo de texto ou sys.stdin e suporta
    a leitura a partir desse fluxo.

    Nota:
        Normalmente, é uma má ideia misturar estes três conjuntos de métodos:

        -- isEmpty(), readInt(), readFloat(), readBool(), readString()

        -- hasNextLine(), readLine()

        -- readAll(), readAllInts(), readAllFloats(), readAllBools(),
           readAllStrings(), readAllLines()

        Geralmente, é melhor usar apenas um conjunto por vez.
    """

    # -------------------------------------------------------------------

    def __init__(self, fileOrUrl=None):
        """Constrói um objeto que encapsula um fluxo de dados.

        O fluxo pode ser um arquivo cujo nome é dado como fileOrUrl, um recurso
        cujo URL é fornecido como fileOrUrl ou sys.stdin por padrão.

        :param fileOrUrl: Nome do arquivo, URL ou None para stdin.
        """
        self._buffer = ""  # Buffer interno para armazenar dados do fluxo
        self._stream = None  # Objeto de fluxo associado
        self._readingWebPage = False  # Indica se está lendo de uma página web

        if fileOrUrl is None:
            self._stream = sys.stdin  # Usa stdin como fluxo padrão
            return

        # Tenta abrir um arquivo, depois uma URL
        try:
            if sys.hexversion < 0x03000000:
                self._stream = open(fileOrUrl, "rU")
            else:
                self._stream = open(fileOrUrl, "r", encoding="utf-8")
        except IOError:
            try:
                self._stream = urllib.urlopen(fileOrUrl)
                self._readingWebPage = True
            except IOError:
                raise IOError(f"Nenhum arquivo ou URL encontrado: {fileOrUrl}")

    # -------------------------------------------------------------------

    def _readRegExp(self, regExp):
        """Descarta os caracteres em branco iniciais do fluxo e lê um padrão.

        Lê do fluxo uma string correspondente à expressão regular regExp.
        Levanta EOFError se não houver mais caracteres não em branco.
        Levanta ValueError se os próximos caracteres não corresponderem à regExp.

        :param regExp: Uma expressão regular.
        :returns: String que corresponde à expressão regular.
        """
        if self.isEmpty():
            raise EOFError("Fluxo de entrada vazio.")

        compiledRegExp = re.compile(r"^\s*" + regExp)
        match = compiledRegExp.search(self._buffer)

        if match is None:
            raise ValueError("Os próximos caracteres não correspondem ao padrão.")

        s = match.group()
        self._buffer = self._buffer[match.end() :]
        return s.lstrip()

    # -------------------------------------------------------------------

    def isEmpty(self):
        """Retorna True se não houver caracteres não em branco no fluxo.

        :returns: True se o fluxo estiver vazio, False caso contrário.
        """
        while self._buffer.strip() == "":
            line = self._stream.readline()

            if sys.hexversion < 0x03000000 or self._readingWebPage:
                line = line.decode("utf-8")

            if line == "":
                return True

            self._buffer += str(line)

        return False

    # -------------------------------------------------------------------

    def readInt(self):
        """Lê um inteiro do fluxo.

        Descarta os caracteres em branco iniciais e lê um inteiro. Levanta
        EOFError se o fluxo estiver vazio e ValueError se os caracteres não
        puderem ser convertidos em um inteiro.

        :returns: Um inteiro lido do fluxo.
        """
        s = self._readRegExp(r"[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)")
        radix = 10
        strLength = len(s)

        if (strLength >= 1) and (s[0:1] == "0"):
            radix = 8
        if (strLength >= 2) and (s[0:2] == "0x"):
            radix = 16
        if (strLength >= 3) and (s[0:3] == "-0x"):
            radix = 16

        return int(s, radix)

    # -------------------------------------------------------------------

    def readAllInts(self):
        """Lê todos os inteiros restantes do fluxo.

        Converte cada string lida em um inteiro e retorna como uma lista.
        Levanta ValueError se alguma string não puder ser convertida.

        :returns: Uma lista de inteiros.
        """
        strings = self.readAllStrings()
        return [int(s) for s in strings]

    # -------------------------------------------------------------------

    def readFloat(self):
        """Lê um valor de ponto flutuante do fluxo.

        Descarta os caracteres em branco iniciais e lê um float. Levanta
        EOFError se o fluxo estiver vazio e ValueError se os caracteres não
        puderem ser convertidos em um float.

        :returns: Um valor float lido do fluxo.
        """
        s = self._readRegExp(r"[-+]?\d*(\.\d+)?([eE][-+]?\d+)?")
        return float(s)

    # -------------------------------------------------------------------

    def readAllFloats(self):
        """Lê todos os valores de ponto flutuante restantes do fluxo.

        Converte cada string lida em um float e retorna como uma lista.
        Levanta ValueError se alguma string não puder ser convertida.

        :returns: Uma lista de floats.
        """
        strings = self.readAllStrings()
        return [float(s) for s in strings]

    # -------------------------------------------------------------------

    def readBool(self):
        """Lê um valor booleano do fluxo.

        Descarta os caracteres em branco iniciais e lê um bool. Levanta
        EOFError se o fluxo estiver vazio e ValueError se os caracteres não
        puderem ser convertidos em um bool.

        :returns: Um valor booleano lido do fluxo.
        """
        s = self._readRegExp(r"(True|False|1|0)")
        return s in ("True", "1")

    # -------------------------------------------------------------------

    def readAllBools(self):
        """Lê todos os valores booleanos restantes do fluxo.

        Converte cada string lida em um bool e retorna como uma lista.
        Levanta ValueError se alguma string não puder ser convertida.

        :returns: Uma lista de valores booleanos.
        """
        strings = self.readAllStrings()
        return [s in ("True", "1") for s in strings]

    # -------------------------------------------------------------------

    def readString(self):
        """Lê uma string do fluxo.

        Descarta os caracteres em branco iniciais e lê uma string. Levanta
        EOFError se o fluxo estiver vazio.

        :returns: Uma string lida do fluxo.
        """
        return self._readRegExp(r"\S+")

    # -------------------------------------------------------------------

    def readAllStrings(self):
        """Lê todas as strings restantes do fluxo.

        Retorna as strings como uma lista.

        :returns: Uma lista de strings.
        """
        strings = []
        while not self.isEmpty():
            strings.append(self.readString())
        return strings

    # -------------------------------------------------------------------

    def hasNextLine(self):
        """Retorna True se houver uma próxima linha no fluxo.

        :returns: True se houver uma próxima linha, False caso contrário.
        """
        if self._buffer != "":
            return True

        self._buffer = self._stream.readline()

        if sys.hexversion < 0x03000000 or self._readingWebPage:
            self._buffer = self._buffer.decode("utf-8")

        return self._buffer != ""

    # -------------------------------------------------------------------

    def readLine(self):
        """Lê e retorna a próxima linha do fluxo como uma string.

        Levanta EOFError se não houver mais linhas.

        :returns: A próxima linha como string.
        """
        if not self.hasNextLine():
            raise EOFError("Não há mais linhas no fluxo.")

        s = self._buffer
        self._buffer = ""
        return s.rstrip("\n")

    # -------------------------------------------------------------------

    def readAllLines(self):
        """Lê todas as linhas restantes do fluxo.

        Retorna as linhas como uma lista de strings.

        :returns: Uma lista de strings.
        """
        lines = []
        while self.hasNextLine():
            lines.append(self.readLine())
        return lines

    # -------------------------------------------------------------------

    def readAll(self):
        """Lê e retorna todo o conteúdo restante do fluxo como uma string.

        :returns: Todo o conteúdo restante do fluxo como string.
        """
        s = self._buffer
        self._buffer = ""

        for line in self._stream:
            if sys.hexversion < 0x03000000 or self._readingWebPage:
                line = line.decode("utf-8")
            s += line

        return s

    # -------------------------------------------------------------------

    def __del__(self):
        """Fecha o fluxo quando o objeto é destruído."""
        if self._stream is not None:
            self._stream.close()


# =======================================================================
# Para testes
# =======================================================================


def _main():
    """Executa testes para a classe InStream.

    O primeiro argumento da linha de comando deve ser o nome do método
    que será chamado. O segundo argumento opcional deve ser o arquivo
    ou URL a ser lido.
    """
    from stdio import writeln

    testId = sys.argv[1]

    if len(sys.argv) > 2:
        inStream = InStream(sys.argv[2])
    else:
        inStream = InStream()

    if testId == "readInt":
        writeln(inStream.readInt())
    elif testId == "readAllInts":
        writeln(inStream.readAllInts())
    elif testId == "readFloat":
        writeln(inStream.readFloat())
    elif testId == "readAllFloats":
        writeln(inStream.readAllFloats())
    elif testId == "readBool":
        writeln(inStream.readBool())
    elif testId == "readAllBools":
        writeln(inStream.readAllBools())
    elif testId == "readString":
        writeln(inStream.readString())
    elif testId == "readAllStrings":
        writeln(inStream.readAllStrings())
    elif testId == "readLine":
        writeln(inStream.readLine())
    elif testId == "readAllLines":
        writeln(inStream.readAllLines())
    elif testId == "readAll":
        writeln(inStream.readAll())


if __name__ == "__main__":
    _main()