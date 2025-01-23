# Created for BADS 2018
# See README.md for details
# This is python3

import struct
import sys

"""
Entrada binária padrão. Esta classe fornece métodos para leitura
de bits da entrada padrão, seja um bit de cada vez (como booleano),
8 bits de cada vez (como char) ou 32 bits de cada vez (como int).

Todos os tipos primitivos são assumidos como representados em ordem big-endian.

O cliente não deve misturar chamadas para BinaryStdIn com chamadas para stdin,
pois isso pode resultar em comportamento inesperado.
"""


class BinaryStdIn:
    """Gerencia a leitura de dados binários da entrada padrão.

    Esta classe fornece métodos para ler bits, bytes, caracteres,
    strings e números inteiros diretamente da entrada padrão,
    assumindo a representação em ordem big-endian.

    Nota:
        - O cliente deve evitar misturar o uso desta classe com chamadas diretas
          para stdin, pois isso pode causar comportamentos inesperados.
    """

    EOF = -1  # Indica o fim do fluxo de entrada
    ins = sys.stdin.buffer  # Define a entrada padrão como buffer binário
    n = 0  # Número de bits restantes no buffer
    buffer_ = 0  # Armazena temporariamente os bits lidos
    is_init = False  # Indica se o buffer foi inicializado

    @staticmethod
    def _initialize():
        """Inicializa o fluxo de entrada binária.

        Configura o buffer e garante que o fluxo de entrada esteja pronto para leitura.
        """
        BinaryStdIn.buffer_ = 0  # Limpa o buffer
        BinaryStdIn.n = 0  # Reinicia o contador de bits
        BinaryStdIn._fill_buffer()  # Preenche o buffer com novos bits
        BinaryStdIn.is_init = True  # Marca como inicializado

    @staticmethod
    def _fill_buffer():
        """Preenche o buffer com os próximos 8 bits da entrada.

        Lê 1 byte (8 bits) da entrada padrão e atualiza o buffer interno.
        Caso a entrada esteja vazia, define o buffer como EOF.
        """
        x = BinaryStdIn.ins.read(1)  # Lê 1 byte da entrada

        if x == b"":  # Verifica se a entrada está vazia
            BinaryStdIn.buffer_ = BinaryStdIn.EOF  # Marca o buffer como EOF
            BinaryStdIn.n = -1  # Define que não há mais bits no buffer
            return

        BinaryStdIn.buffer_ = struct.unpack("B", x)[0]  # Converte o byte para inteiro
        BinaryStdIn.n = 8  # Reinicia o contador de bits no buffer

    @staticmethod
    def close():
        """Fecha este fluxo de entrada e libera quaisquer recursos do sistema associados."""
        if not BinaryStdIn.is_init:  # Inicializa se ainda não foi feito
            BinaryStdIn._initialize()

        BinaryStdIn.ins.close()  # Fecha o fluxo de entrada
        BinaryStdIn.is_init = False  # Marca como não inicializado

    @staticmethod
    def is_empty():
        """Verifica se o fluxo de entrada está vazio.

        :returns: True se a entrada padrão estiver vazia, False caso contrário.
        """
        if not BinaryStdIn.is_init:  # Inicializa se ainda não foi feito
            BinaryStdIn._initialize()

        return BinaryStdIn.buffer_ == BinaryStdIn.EOF  # Retorna True se EOF

    @staticmethod
    def read_bool():
        """Lê um único bit como um valor booleano.

        :returns: True ou False representando o bit lido.
        :raises EOFError: Se o fluxo de entrada estiver vazio.
        """
        if BinaryStdIn.is_empty():  # Verifica se a entrada está vazia
            raise EOFError("Lendo de um fluxo de entrada vazio")

        BinaryStdIn.n -= 1  # Decrementa o contador de bits no buffer
        bit = ((BinaryStdIn.buffer_ >> BinaryStdIn.n) & 1) == 1  # Extrai o próximo bit

        if BinaryStdIn.n == 0:  # Recarrega o buffer se não houver mais bits
            BinaryStdIn._fill_buffer()

        return bit

    @staticmethod
    def read_char():
        """Lê o próximo caractere de 8 bits da entrada padrão.

        :returns: O caractere lido.
        :raises EOFError: Se o fluxo de entrada estiver vazio.
        """
        if BinaryStdIn.is_empty():  # Verifica se a entrada está vazia
            raise EOFError("Lendo de um fluxo de entrada vazio")

        if BinaryStdIn.n == 8:  # Verifica se há 8 bits completos no buffer
            x = BinaryStdIn.buffer_  # Obtém o byte completo
            BinaryStdIn._fill_buffer()  # Recarrega o buffer
            return chr(x & 0xFF)  # Retorna o caractere correspondente

        x = BinaryStdIn.buffer_  # Obtém os bits restantes no buffer
        x <<= 8 - BinaryStdIn.n  # Move os bits para a posição correta
        oldN = BinaryStdIn.n  # Salva o estado atual do contador

        if BinaryStdIn.is_empty():  # Verifica novamente se a entrada está vazia
            raise EOFError("Lendo de um fluxo de entrada vazio")

        BinaryStdIn._fill_buffer()  # Recarrega o buffer
        BinaryStdIn.n = oldN  # Restaura o estado do contador
        x |= BinaryStdIn.buffer_ >> BinaryStdIn.n  # Combina os bits do novo buffer

        return chr(x & 0xFF)  # Retorna o caractere correspondente

    @staticmethod
    def read_string():
        """Lê uma string completa da entrada padrão.

        A leitura continua até que o fluxo de entrada esteja vazio.

        :returns: A string lida.
        :raises EOFError: Se o fluxo de entrada estiver vazio.
        """
        if BinaryStdIn.is_empty():  # Verifica se a entrada está vazia
            raise EOFError("Lendo de um fluxo de entrada vazio")

        sb = ""  # Inicializa a string resultante

        while not BinaryStdIn.is_empty():  # Continua enquanto houver dados
            sb += BinaryStdIn.read_char()  # Adiciona o próximo caractere

        return sb

    @staticmethod
    def read_int(r=32):
        """Lê um número inteiro da entrada padrão.

        :param r: O número de bits a serem lidos. O padrão é 32.
        :returns: O inteiro lido.
        :raises ValueError: Se r estiver fora do intervalo [1, 32].
        :raises EOFError: Se o fluxo de entrada estiver vazio.
        """
        if r == 32:  # Lê um inteiro de 32 bits (4 bytes)
            x = 0  # Inicializa o inteiro resultante

            for _ in range(0, 4):  # Itera sobre os 4 bytes
                c = BinaryStdIn.read_char()  # Lê o próximo caractere
                x <<= 8  # Move os bits existentes para a esquerda
                x |= ord(c)  # Adiciona o valor do novo byte

            return x

        if r < 1 or r > 32:  # Verifica se o valor de r é válido
            raise ValueError(f"Valor inválido para r = {r}")

        x = 0  # Inicializa o inteiro resultante

        for _ in range(0, r):  # Itera sobre os bits especificados
            x <<= 1  # Move os bits existentes para a esquerda
            bit = BinaryStdIn.read_bool()  # Lê o próximo bit

            if bit:  # Adiciona o bit ao resultado
                x |= 1

        return x


def main():
    """Executa um exemplo de leitura da entrada padrão.

    Lê caracteres da entrada padrão usando BinaryStdIn e escreve-os
    na saída padrão usando BinaryStdOut.
    """
    from binary_stdout import BinaryStdOut

    while not BinaryStdIn.is_empty():  # Continua enquanto houver dados
        BinaryStdOut.write_char(BinaryStdIn.read_char())  # Lê e escreve cada caractere


if __name__ == "__main__":
    main()