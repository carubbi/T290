# Created for BADS 2018
# See README.md for details
# This is python3
import sys


class BoyerMoore:
    """
    A classe BoyerMoore encontra a primeira ocorrência de uma string padrão em uma string de texto.

    Esta implementação utiliza o algoritmo Boyer-Moore (com a regra de caractere ruim, mas sem a regra forte de sufixo bom).
    """

    def __init__(self, pat):
        """
        Pré-processa a string padrão.

        :param pat: a string padrão
        """
        self.pat = pat
        M = len(pat)
        R = 256
        self.right = [-1 for i in range(0, R)]  # -1 para caracteres que não estão no padrão
        for j in range(0, M):
            self.right[ord(pat[j])] = j

    def search(self, txt):
        """
        Retorna o índice da primeira ocorrência da string padrão na string de texto.

        :param txt: a string de texto
        :return: o índice da primeira ocorrência da string padrão na string de texto; N se não houver correspondência
        """
        N = len(txt)
        M = len(self.pat)
        skip = 0
        i = 0
        while i <= N - M:
            skip = 0
            for j in range(M - 1, -1, -1):
                if not (self.pat[j] == txt[i + j]):
                    skip = j - self.right[ord(txt[i + j])]
                    if skip < 1:
                        skip = 1
                    break
            if skip == 0:
                return i
            i += skip
        return N


def main():
    """
    Recebe uma string padrão e uma string de entrada como argumentos de linha de comando;
    busca a string padrão na string de texto; e imprime a primeira ocorrência
    da string padrão na string de texto.

    Imprime o padrão após o final da string caso nenhuma correspondência seja encontrada.
    """
    pat = sys.argv[1]
    txt = sys.argv[2]
    bm = BoyerMoore(pat)
    print("text:    {}".format(txt))
    offset = bm.search(txt)
    print("pattern:", end=" ")
    for _ in range(0, offset):
        print("", end=" ")
    print(pat)


if __name__ == "__main__":
    main()
