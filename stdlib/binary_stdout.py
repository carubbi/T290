# Created for BADS 2018
# See README.md for details
# This is python3

import struct
import sys

"""
Saída binária padrão. Esta classe fornece métodos para converter
algumas variáveis de tipos primitivos (booleano, byte, char e int)
em sequências de bits e escrevê-las em um fluxo de saída.
O fluxo de saída pode ser a saída padrão ou outro fluxo de saída.
Usa big-endian (byte mais significativo primeiro).

O cliente deve chamar flush() no fluxo de saída ao terminar de escrever os bits.

O cliente não deve misturar chamadas para BinaryOut com chamadas para stdout;
do contrário, um comportamento inesperado pode ocorrer.
"""


class BinaryStdOut:
    """Gerencia a saída de dados binários para um fluxo de saída.

    Fornece métodos para escrever bits individuais, bytes, inteiros, caracteres
    e strings em um fluxo de saída. O formato de saída utiliza a ordem de bytes
    big-endian (byte mais significativo primeiro).

    O usuário deve chamar explicitamente `flush` após a escrita para garantir
    que todos os dados no buffer sejam corretamente gravados no fluxo de saída.

    """

    out = sys.stdout.buffer  # Define a saída binária padrão
    buffer_ = 0  # Buffer de 8 bits para armazenar os dados temporariamente
    n = 0  # Número de bits usados no buffer
    is_init = False  # Indica se o buffer foi inicializado

    @staticmethod
    def _initialize():
        """Inicializa o sistema de saída binária.

        Configura o buffer de bits e marca o sistema como inicializado.
        """
        BinaryStdOut.buffer_ = 0  # Limpa o buffer
        BinaryStdOut.n = 0  # Reinicia o contador de bits no buffer
        BinaryStdOut.is_init = True  # Marca como inicializado

    @staticmethod
    def _write_bit(x):
        """Escreve um único bit no buffer.

        Quando o buffer atinge 8 bits, ele é automaticamente gravado
        no fluxo de saída.

        :param x: O bit para gravar (0 ou 1).
        """
        if not BinaryStdOut.is_init:  # Inicializa se ainda não foi feito
            BinaryStdOut._initialize()

        BinaryStdOut.buffer_ <<= 1  # Move o buffer para a esquerda

        if x:  # Define o bit menos significativo como 1 se x for True
            BinaryStdOut.buffer_ |= 1

        BinaryStdOut.n += 1  # Incrementa o contador de bits

        if BinaryStdOut.n == 8:  # Se o buffer estiver cheio, grava os dados
            BinaryStdOut._clear_buffer()

    @staticmethod
    def _write_byte(x):
        """Escreve um único byte no fluxo de saída.

        Se o buffer estiver vazio, o byte é gravado diretamente. Caso contrário,
        o byte é dividido e escrito bit a bit.

        :param x: O byte para gravar (inteiro entre 0 e 255).
        :raises AssertionError: Se o byte estiver fora do intervalo válido.
        """
        if not BinaryStdOut.is_init:  # Inicializa se ainda não foi feito
            BinaryStdOut._initialize()

        assert x >= 0 and x < 256  # Verifica se o byte está no intervalo permitido

        if BinaryStdOut.n == 0:  # Escreve diretamente se o buffer estiver vazio
            BinaryStdOut.out.write(struct.pack("B", x))
            return

        # Caso contrário, grava um bit por vez
        for i in range(0, 8):
            bit = ((x >> (8 - i - 1)) & 1) == 1  # Extrai cada bit do byte
            BinaryStdOut._write_bit(bit)

    @staticmethod
    def _clear_buffer():
        """Grava o buffer atual no fluxo de saída.

        Preenche os bits restantes no buffer com zeros para formar um byte completo
        e grava o byte no fluxo de saída. O buffer é então limpo.
        """
        if not BinaryStdOut.is_init:  # Inicializa se ainda não foi feito
            BinaryStdOut._initialize()

        if BinaryStdOut.n == 0:  # Retorna se o buffer estiver vazio
            return

        if BinaryStdOut.n > 0:  # Preenche o buffer com zeros
            BinaryStdOut.buffer_ <<= 8 - BinaryStdOut.n

        BinaryStdOut.out.write(struct.pack("B", BinaryStdOut.buffer_))  # Grava o byte

        BinaryStdOut.n = 0  # Reinicia o contador de bits
        BinaryStdOut.buffer_ = 0  # Limpa o buffer

    @staticmethod
    def flush():
        """Descarrega o buffer no fluxo de saída e garante que todos os dados sejam gravados."""
        BinaryStdOut._clear_buffer()
        BinaryStdOut.out.flush()

    @staticmethod
    def close():
        """Fecha o fluxo de saída após descarregar todos os dados."""
        BinaryStdOut.flush()
        BinaryStdOut.out.close()
        BinaryStdOut.is_init = False  # Marca como não inicializado

    @staticmethod
    def write_bool(x):
        """Escreve um valor booleano como um único bit.

        :param x: O valor booleano para gravar (True ou False).
        """
        BinaryStdOut._write_bit(x)

    @staticmethod
    def write_byte(x):
        """Escreve um único byte no fluxo de saída.

        :param x: O byte para gravar (inteiro entre 0 e 255).
        """
        BinaryStdOut._write_byte(x & 0xFF)

    @staticmethod
    def write_int(x, r=32):
        """Escreve um inteiro no fluxo de saída.

        O inteiro é escrito como um conjunto de r bits, com o padrão sendo 32 bits.

        :param x: O inteiro a ser escrito.
        :param r: O número de bits a serem escritos. O padrão é 32.
        :raises ValueError: Se r estiver fora do intervalo permitido ou x não for compatível.
        """
        if r == 32:  # Escreve como 4 bytes para 32 bits
            BinaryStdOut._write_byte(((x >> 24) & 0xFF))
            BinaryStdOut._write_byte(((x >> 16) & 0xFF))
            BinaryStdOut._write_byte(((x >> 8) & 0xFF))
            BinaryStdOut._write_byte(((x >> 0) & 0xFF))
            return

        if r < 1 or r > 16:  # Verifica se r está no intervalo permitido
            raise ValueError(f"Valor inválido para r = {r}")

        if x < 0 or x >= (1 << r):  # Verifica se x é compatível com r bits
            raise ValueError(f"Valor inválido para {r}-bit char = {x}")

        for i in range(0, r):
            bit = ((x >> (r - i - 1)) & 1) == 1  # Extrai cada bit
            BinaryStdOut._write_bit(bit)

    @staticmethod
    def write_char(x, r=8):
        """Escreve um caractere no fluxo de saída.

        O caractere pode ser escrito com um tamanho especificado (padrão: 8 bits).

        :param x: O caractere a ser escrito.
        :param r: O número de bits a serem usados para representar o caractere.
        :raises ValueError: Se x ou r forem inválidos.
        """
        if r == 8:  # Caso padrão: 8 bits
            if ord(x) < 0 or ord(x) >= 256:
                raise ValueError(f"Caractere ilegal de 8 bits = {x}")

            BinaryStdOut._write_byte(ord(x))
            return

        if r < 1 or r > 16:  # Verifica se r está no intervalo permitido
            raise ValueError(f"Valor inválido para r = {r}")

        if ord(x) >= (1 << r):  # Verifica se o caractere é compatível com r bits
            raise ValueError(f"Caractere ilegal de {r} bits = {x}")

        for i in range(0, r):
            bit = ((ord(x) >> (r - i - 1)) & 1) == 1
            BinaryStdOut._write_bit(bit)

    @staticmethod
    def write_string(s, r=8):
        """Escreve uma string no fluxo de saída.

        Cada caractere na string é escrito usando r bits (padrão: 8 bits).

        :param s: A string a ser escrita.
        :param r: O número de bits para cada caractere.
        """
        for i in s:
            BinaryStdOut.write_char(i, r)


def main():
    """Executa um caso de teste para a classe BinaryStdOut.

    Lê caracteres fornecidos como argumentos de linha de comando e os escreve
    no fluxo de saída usando BinaryStdOut.
    """
    for i in sys.argv[1]:
        BinaryStdOut.write_char(i)
    BinaryStdOut.close()


if __name__ == "__main__":
    main()