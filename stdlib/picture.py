# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""picture.py.

O módulo picture define a classe Picture.

"""

# -----------------------------------------------------------------------

import pygame. color

# -----------------------------------------------------------------------

_DEFAULT_WIDTH = 512  # Largura padrão da imagem
_DEFAULT_HEIGHT = 512  # Altura padrão da imagem

# -----------------------------------------------------------------------


class Picture:
    """Um objeto Picture modela uma imagem.

    Ele é inicializado com uma largura e altura especificadas e contém
    todos os pixels pretos. Posteriormente, é possível carregar uma imagem
    a partir de um arquivo JPG ou PNG.

    """

    def __init__(self, arg1=None, arg2=None):
        """Constrói uma imagem.

        - Se arg1 e arg2 forem None, cria uma imagem toda preta com largura
          _DEFAULT_WIDTH e altura _DEFAULT_HEIGHT.
        - Se arg1 for fornecido e arg2 for None, carrega uma imagem do
          arquivo especificado em arg1.
        - Se arg1 e arg2 forem fornecidos, cria uma imagem toda preta com
          largura arg1 e altura arg2.

        :param arg1: Nome do arquivo ou largura da imagem.
        :param arg2: Altura da imagem (opcional).
        :raises ValueError: Se os argumentos forem inválidos.
        :raises IOError: Se o arquivo especificado não puder ser carregado.
        """
        if (arg1 is None) and (arg2 is None):
            maxW = _DEFAULT_WIDTH
            maxH = _DEFAULT_HEIGHT
            self._surface = pygame.Surface((maxW, maxH))  # Cria uma superfície preta
            self._surface.fill((0, 0, 0))
        elif (arg1 is not None) and (arg2 is None):
            fileName = arg1
            try:
                self._surface = pygame.image.load(fileName)  # Carrega a imagem
            except pygame.error:
                raise IOError(f"Não foi possível carregar o arquivo: {fileName}")
        elif (arg1 is not None) and (arg2 is not None):
            maxW = arg1
            maxH = arg2
            self._surface = pygame.Surface((maxW, maxH))  # Cria uma superfície preta
            self._surface.fill((0, 0, 0))
        else:
            raise ValueError("Argumentos inválidos para o construtor.")

    # -------------------------------------------------------------------

    def save(self, f):
        """Salva a imagem atual no arquivo especificado.

        :param f: Nome do arquivo de saída.
        """
        pygame.image.save(self._surface, f)

    # -------------------------------------------------------------------

    def width(self):
        """Retorna a largura da imagem.

        :returns: A largura da imagem em pixels.
        """
        return self._surface.get_width()

    # -------------------------------------------------------------------

    def height(self):
        """Retorna a altura da imagem.

        :returns: A altura da imagem em pixels.
        """
        return self._surface.get_height()

    # -------------------------------------------------------------------

    def get(self, x, y):
        """Retorna a cor do pixel na posição (x, y).

        :param x: Coordenada x do pixel.
        :param y: Coordenada y do pixel.
        :returns: Um objeto Color representando a cor do pixel.
        """
        pygameColor = self._surface.get_at((x, y))  # Obtém a cor do pixel
        return color.Color(pygameColor.r, pygameColor.g, pygameColor.b)

    # -------------------------------------------------------------------

    def set(self, x, y, c):
        """Define a cor do pixel na posição (x, y).

        :param x: Coordenada x do pixel.
        :param y: Coordenada y do pixel.
        :param c: Um objeto Color representando a nova cor do pixel.
        """
        pygameColor = pygame.Color(c.getRed(), c.getGreen(), c.getBlue(), 0)
        self._surface.set_at((x, y), pygameColor)  # Define a nova cor do pixel

# -----------------------------------------------------------------------
# Função principal para testes
# -----------------------------------------------------------------------

def main():
    """Executa testes para a classe Picture.

    Cria uma imagem, define algumas cores e salva o resultado.
    """
    pygame.init()

    # Cria uma imagem preta com tamanho padrão
    pic = Picture()

    # Define algumas cores
    pic.set(100, 100, color.RED)
    pic.set(200, 200, color.GREEN)
    pic.set(300, 300, color.BLUE)

    # Salva a imagem em um arquivo
    pic.save("output.png")
    print("Imagem salva como 'output.png'.")

    pygame.quit()


if __name__ == "__main__":
    main()