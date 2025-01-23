# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""stddraw.py.

O módulo stddraw fornece funções para criar desenhos gráficos, manipular eventos
e gerenciar janelas gráficas.

"""

import pygame
import time

# -----------------------------------------------------------------------
# Configurações iniciais
# -----------------------------------------------------------------------

_WIDTH = 512  # Largura padrão da janela
_HEIGHT = 512  # Altura padrão da janela
_XMIN = 0.0  # Valor mínimo no eixo x
_XMAX = 1.0  # Valor máximo no eixo x
_YMIN = 0.0  # Valor mínimo no eixo y
_YMAX = 1.0  # Valor máximo no eixo y

_COLOR = pygame.Color(0, 0, 0)  # Cor inicial: preto
_surface = None  # Superfície para desenhos
_window = None  # Janela gráfica

# -----------------------------------------------------------------------
# Inicialização
# -----------------------------------------------------------------------

pygame.init()
pygame.font.init()

# -----------------------------------------------------------------------
# Funções para gerenciar janelas e superfícies
# -----------------------------------------------------------------------

def setCanvasSize(width, height):
    """Define o tamanho da janela de desenho.

    :param width: Largura da janela em pixels.
    :param height: Altura da janela em pixels.
    """
    global _surface, _window

    _surface = pygame.Surface((width, height))  # Cria uma superfície para desenho
    _window = pygame.display.set_mode((width, height))  # Define o tamanho da janela

# Define a janela com dimensões padrão na inicialização
setCanvasSize(_WIDTH, _HEIGHT)


# -----------------------------------------------------------------------

def setXscale(min_, max_):
    """Define a escala para o eixo x.

    :param min_: Valor mínimo no eixo x.
    :param max_: Valor máximo no eixo x.
    """
    global _XMIN, _XMAX
    _XMIN = min_
    _XMAX = max_


# -----------------------------------------------------------------------

def setYscale(min_, max_):
    """Define a escala para o eixo y.

    :param min_: Valor mínimo no eixo y.
    :param max_: Valor máximo no eixo y.
    """
    global _YMIN, _YMAX
    _YMIN = min_
    _YMAX = max_


# -----------------------------------------------------------------------

def clear():
    """Limpa a superfície de desenho, preenchendo-a com branco."""
    _surface.fill(pygame.Color(255, 255, 255))


# -----------------------------------------------------------------------
# Conversão de coordenadas
# -----------------------------------------------------------------------

def _scaleX(x):
    """Converte uma coordenada x para pixel.

    :param x: Coordenada no sistema de coordenadas definido.
    :returns: Coordenada em pixels.
    """
    return int(_WIDTH * (x - _XMIN) / (_XMAX - _XMIN))


# -----------------------------------------------------------------------

def _scaleY(y):
    """Converte uma coordenada y para pixel.

    :param y: Coordenada no sistema de coordenadas definido.
    :returns: Coordenada em pixels.
    """
    return int(_HEIGHT * (_YMAX - y) / (_YMAX - _YMIN))


# -----------------------------------------------------------------------
# Funções para desenhar formas
# -----------------------------------------------------------------------

def point(x, y):
    """Desenha um ponto na coordenada especificada.

    :param x: Coordenada x do ponto.
    :param y: Coordenada y do ponto.
    """
    pixel_x = _scaleX(x)
    pixel_y = _scaleY(y)
    _surface.set_at((pixel_x, pixel_y), _COLOR)


# -----------------------------------------------------------------------

def line(x0, y0, x1, y1):
    """Desenha uma linha entre dois pontos.

    :param x0: Coordenada x do ponto inicial.
    :param y0: Coordenada y do ponto inicial.
    :param x1: Coordenada x do ponto final.
    :param y1: Coordenada y do ponto final.
    """
    pixel_x0 = _scaleX(x0)
    pixel_y0 = _scaleY(y0)
    pixel_x1 = _scaleX(x1)
    pixel_y1 = _scaleY(y1)
    pygame.draw.line(_surface, _COLOR, (pixel_x0, pixel_y0), (pixel_x1, pixel_y1))


# -----------------------------------------------------------------------
# Funções auxiliares para gerenciamento de eventos
# -----------------------------------------------------------------------

def show():
    """Exibe a superfície de desenho na janela gráfica."""
    _window.blit(_surface, (0, 0))
    pygame.display.update()


# -----------------------------------------------------------------------
# Função principal para testes
# -----------------------------------------------------------------------

def main():
    """Executa testes para as funções do módulo stddraw.

    Desenha formas simples na janela gráfica para demonstração.
    """
    clear()

    # Desenha uma linha diagonal
    line(0.0, 0.0, 1.0, 1.0)

    # Desenha um ponto no centro da janela
    point(0.5, 0.5)

    # Exibe os desenhos
    show()

    # Aguarda 5 segundos antes de fechar a janela
    time.sleep(5)


if __name__ == "__main__":
    main()