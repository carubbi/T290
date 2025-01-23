# Created for BADS 2018
# See README.md for details
# This is python3
import struct
import sys

"""
Esta classe fornece métodos para converter algumas variáveis de tipos primitivos 
(booleano, byte, char e int) em sequências de bits e escrevê-las em um fluxo de saída.
O fluxo de saída pode ser a saída padrão ou outro fluxo de saída. 
Usa big-endian (byte mais significativo primeiro).

O cliente deve chamar flush() no fluxo de saída ao terminar de escrever os bits.

O cliente não deve misturar chamadas para BinaryOut com chamadas para stdout;
do contrário, um comportamento inesperado pode ocorrer.
"""


class BinaryOut:
    """Gerencia a saída de dados binários para um fluxo de saída.

    Fornece métodos para escrever bits individuais, bytes, inteiros, caracteres
    e strings em um fluxo de saída. O formato de saída utiliza a ordem de bytes
    big-endian (byte mais significativo primeiro).

    O usuário deve chamar explicitamente `flush` após a escrita para garantir
    que todos os dados no buffer sejam corretamente gravados no fluxo de saída.

    """

    def __init__(self, os=sys.stdout):
        """Inicializa um fluxo de saída binário.

        Por padrão, grava na saída padrão caso nenhum fluxo de saída seja fornecido.

        :param os: O fluxo de saída para gravar. O padrão é sys.stdout.

        """
        self.out = os.buffer
        self.buffer = 0  # Buffer de 8 bits para gravar os bits
        self.n = 0  # Número de bits usados no buffer

    def _writeBit(self, x):
        """Escreve um único bit no buffer.

        Quando o buffer está cheio (8 bits), ele é automaticamente gravado
        no fluxo de saída.

        :param x: O bit para gravar (0 ou 1).
        """
        self.buffer <<= 1
        if x:
            self.buffer |= 1
        self.n += 1
        if self.n == 8:
            self._clearBuffer()

    def _writeByte(self, x):
        """Escreve um único byte no fluxo de saída.

        Se o buffer estiver vazio, o byte é gravado diretamente. Caso contrário,
        o byte é gravado bit a bit.

        :param x: O byte para gravar (inteiro entre 0 e 255).
        :raises AssertionError: Se o byte estiver fora do intervalo válido.
        """
        assert x >= 0 and x < 256
        # Otimizado se estiver alinhado a byte
        if self.n == 0:
            self.out.write(struct.pack("B", x))
            return
        # Caso contrário, grava um bit por vez
        for i in range(0, 8):
            bit = ((x >> (8 - i - 1)) & 1) == 1
            self._writeBit(bit)

    def _clearBuffer(self):
        """Grava o buffer atual no fluxo de saída.

        Se o buffer não estiver vazio, seu conteúdo é preenchido com zeros
        para formar um byte completo e, em seguida, gravado no fluxo de saída.
        Após a gravação, o buffer é limpo.
        """
        if self.n == 0:
            return
        if self.n > 0:
            self.buffer <<= 8 - self.n
        self.out.write(self.buffer.to_bytes(1, "big"))
        self.n = 0
        self.buffer = 0

    def flush(self):
        """Descarrega o buffer de saída.

        Garante que todos os bits no buffer sejam gravados no fluxo de saída
        e limpa o buffer. O fluxo de saída também é descarregado para garantir
        que todos os dados sejam fisicamente gravados.
        """
        self._clearBuffer()
        self.out.flush()

    def close(self):
        """Fecha o fluxo de saída.

        Descarrega o buffer antes de fechar o fluxo de saída.
        """
        self.flush()
        self.out.close()

    def write_bool(self, x):
        """Escreve um valor booleano como um único bit.

        :param x: O valor booleano para gravar (True ou False).
        """
        self._writeBit(x)

    def write_byte(self, x):
        """Escreve um único byte no fluxo de saída.

        :param x: O byte para gravar (inteiro entre 0 e 255).
        """
        self._writeByte(x & 0xFF)

    def write_int(self, x):
        """Escreve um inteiro de 32 bits no fluxo de saída.

        O inteiro é gravado como quatro bytes em ordem big-endian.

        :param x: O inteiro para gravar.
        """
        self._writeByte(((x >> 24) & 0xFF))
        self._writeByte(((x >> 16) & 0xFF))
        self._writeByte(((x >> 8) & 0xFF))
        self._writeByte(((x >> 0) & 0xFF))

    def write_char(self, x):
        """Escreve um único caractere como um valor de 8 bits.

        :param x: O caractere para gravar.
        :raises ValueError: Se o caractere não for um valor válido de 8 bits.
        """
        if ord(x) < 0 or ord(x) >= 256:
            raise ValueError("Caractere ilegal de 8 bits = {}".format(x))
        self._writeByte(ord(x))

    def write_string(self, s):
        """Escreve uma string como uma sequência de caracteres.

        Cada caractere na string é gravado como um valor de 8 bits.

        :param s: A string para gravar.
        """
        for i in s:
            self.write_char(i)


def main():
    """Executa um caso de teste para a classe BinaryOut.

    Grava caracteres fornecidos como argumentos de linha de comando no fluxo de saída.
    """
    out = BinaryOut()
    for i in sys.argv[1]:
        out.write_char(i)
    out.close()


if __name__ == "__main__":
    main()