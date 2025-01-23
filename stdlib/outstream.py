# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""outstream.py.

O módulo outstream define a classe OutStream.

"""

import sys

# -----------------------------------------------------------------------


class OutStream:
    """Um objeto OutStream encapsula um arquivo de texto ou sys.stdout e suporta
    a escrita nesse fluxo.
    """

    # -------------------------------------------------------------------

    def __init__(self, f=None):
        """Constrói um objeto que encapsula um fluxo de saída.

        Se f for fornecido, o fluxo será um arquivo com esse nome.
        Caso contrário, o fluxo será a saída padrão (stdout).

        :param f: Nome do arquivo ou None para stdout.
        """
        if f is None:
            self._stream = sys.stdout  # Define stdout como fluxo padrão
        else:
            if sys.hexversion < 0x03000000:
                self._stream = open(f, "w")  # Abre o arquivo no modo escrita
            else:
                self._stream = open(f, "w", encoding="utf-8")  # Usa codificação UTF-8

    # -------------------------------------------------------------------

    def writeln(self, x=""):
        """Escreve x seguido de uma quebra de linha no fluxo encapsulado.

        :param x: O texto a ser escrito.
        """
        if sys.hexversion < 0x03000000:
            print("Erro: Requer Python 3.", file=sys.stderr)
            sys.exit(1)
        else:
            x = str(x)  # Converte o objeto para string

        self._stream.write(x)  # Escreve o texto no fluxo
        self._stream.write("\n")  # Adiciona a quebra de linha
        self._stream.flush()  # Garante que os dados sejam gravados imediatamente

    # -------------------------------------------------------------------

    def write(self, x=""):
        """Escreve x no fluxo encapsulado sem adicionar uma quebra de linha.

        :param x: O texto a ser escrito.
        """
        if sys.hexversion < 0x03000000:
            print("Erro: Requer Python 3.", file=sys.stderr)
            sys.exit(1)
        else:
            x = str(x)  # Converte o objeto para string

        self._stream.write(x)  # Escreve o texto no fluxo
        self._stream.flush()  # Garante que os dados sejam gravados imediatamente

    # -------------------------------------------------------------------

    def writef(self, fmt, *args):
        """Escreve cada elemento de args no fluxo encapsulado.

        Usa o formato especificado pela string fmt.

        :param fmt: A string de formato.
        :param args: Os argumentos a serem formatados e escritos.
        """
        x = fmt % args  # Formata a string usando os argumentos

        if sys.hexversion < 0x03000000:
            print("Erro: Requer Python 3.", file=sys.stderr)
            sys.exit(1)

        self._stream.write(x)  # Escreve a string formatada no fluxo
        self._stream.flush()  # Garante que os dados sejam gravados imediatamente

    # -------------------------------------------------------------------

    def __del__(self):
        """Fecha o fluxo encapsulado quando o objeto é destruído."""
        self._stream.close()


# -----------------------------------------------------------------------
# Função principal para testes
# -----------------------------------------------------------------------

def main():
    """Executa um caso de teste para a classe OutStream.

    Testa os métodos writeln, write e writef escrevendo para stdout.
    """
    out = OutStream()

    # Testando writeln
    out.writeln("Teste de writeln: Olá, Mundo!")

    # Testando write
    out.write("Teste de write: Sem quebra de linha. ")
    out.write("Continua na mesma linha.\n")

    # Testando writef
    out.writef("Teste de writef: %d + %d = %d\n", 2, 3, 2 + 3)


if __name__ == "__main__":
    main()