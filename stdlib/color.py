# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""color.py.

O módulo color define a classe Color e alguns objetos de cores populares.

"""

# -----------------------------------------------------------------------


class Color:
    """Um objeto Color modela uma cor RGB."""

    # -------------------------------------------------------------------

    def __init__(self, r=0, g=0, b=0):
        """Constrói o objeto com os componentes vermelho (r), verde (g) e azul (b) especificados.

        :param r: Componente vermelho da cor (0-255).
        :param g: Componente verde da cor (0-255).
        :param b: Componente azul da cor (0-255).
        """
        self._r = r  # Componente vermelho
        self._g = g  # Componente verde
        self._b = b  # Componente azul

    # -------------------------------------------------------------------

    def getRed(self):
        """Retorna o componente vermelho da cor.

        :returns: Componente vermelho (0-255).
        """
        return self._r

    # -------------------------------------------------------------------

    def getGreen(self):
        """Retorna o componente verde da cor.

        :returns: Componente verde (0-255).
        """
        return self._g

    # -------------------------------------------------------------------

    def getBlue(self):
        """Retorna o componente azul da cor.

        :returns: Componente azul (0-255).
        """
        return self._b

    # -------------------------------------------------------------------

    def __str__(self):
        """Retorna a representação em string da cor no formato "(r, g, b)".

        :returns: Representação textual da cor.
        """
        return f"({self._r}, {self._g}, {self._b})"


# -----------------------------------------------------------------------

# Alguns objetos Color predefinidos:

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)

RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

CYAN = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW = Color(255, 255, 0)

DARK_RED = Color(128, 0, 0)
DARK_GREEN = Color(0, 128, 0)
DARK_BLUE = Color(0, 0, 128)

GRAY = Color(128, 128, 128)
DARK_GRAY = Color(64, 64, 64)
LIGHT_GRAY = Color(192, 192, 192)

ORANGE = Color(255, 200, 0)
VIOLET = Color(238, 130, 238)
PINK = Color(255, 175, 175)

# Tons de azul usados em Introduction to Programming in Java.
# Pantone 300U. Os valores RGB são aproximadamente (9, 90, 166).
BOOK_BLUE = Color(9, 90, 166)
BOOK_LIGHT_BLUE = Color(103, 198, 243)

# Tons de vermelho usados em Algorithms 4th edition
BOOK_RED = Color(150, 35, 31)

# -----------------------------------------------------------------------


def _main():
    """Executa testes para a classe Color.

    Exibe uma cor predefinida e seus componentes RGB no console.
    """
    from stdio import writeln

    c1 = Color(128, 128, 128)  # Cria uma cor cinza
    writeln(c1)  # Exibe a representação textual da cor
    writeln(c1.getRed())  # Exibe o componente vermelho
    writeln(c1.getGreen())  # Exibe o componente verde
    writeln(c1.getBlue())  # Exibe o componente azul


if __name__ == "__main__":
    _main()