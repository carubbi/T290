"""stdstats.py.

O módulo stdstats define funções relacionadas à análise estatística
 e exibição gráfica de dados.

"""

import math, stddraw

# -----------------------------------------------------------------------

def mean(a):
    """
    Retorna a média dos elementos do array a.

    :param a: Lista de números.
    :returns: A média dos elementos na lista.
    """
    return sum(a) / float(len(a))

# -----------------------------------------------------------------------

def var(a):
    """
    Retorna a variância amostral dos elementos do array a.

    :param a: Lista de números.
    :returns: A variância amostral dos elementos na lista.
    """
    mu = mean(a)
    total = 0.0
    for x in a:
        total += (x - mu) ** 2
    return total / (float(len(a)) - 1.0)

# -----------------------------------------------------------------------

def stddev(a):
    """
    Retorna o desvio padrão dos elementos do array a.

    :param a: Lista de números.
    :returns: O desvio padrão dos elementos na lista.
    """
    return math.sqrt(var(a))

# -----------------------------------------------------------------------

def median(a):
    """
    Retorna a mediana dos elementos do array a.

    :param a: Lista de números.
    :returns: A mediana dos elementos na lista.
    """
    b = list(a)  # Faz uma cópia de a.
    b.sort()
    length = len(b)
    if length % 2 == 1:
        return b[length // 2]
    else:
        return float(b[length // 2 - 1] + b[length // 2]) / 2.0

# -----------------------------------------------------------------------

def min(a):
    """
    Retorna o valor mínimo no array a.

    :param a: Lista de números.
    :returns: O valor mínimo na lista.
    """
    minimum = float("inf")
    for x in a:
        if x < minimum:
            minimum = x
    return minimum

# -----------------------------------------------------------------------

def max(a):
    """
    Retorna o valor máximo no array a.

    :param a: Lista de números.
    :returns: O valor máximo na lista.
    """
    maximum = float("-inf")
    for x in a:
        if x > maximum:
            maximum = x
    return maximum

# -----------------------------------------------------------------------

def plotPoints(a):
    """
    Plota os elementos do array a como pontos.

    :param a: Lista de números a serem plotados.
    :returns: None
    """
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setPenRadius(1.0 / (3.0 * n))
    for i in range(n):
        stddraw.point(i, a[i])

# -----------------------------------------------------------------------

def plotLines(a):
    """
    Plota os elementos do array a como extremidades de linhas.

    :param a: Lista de números a serem plotados.
    :returns: None
    """
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setPenRadius(0.0)
    for i in range(1, n):
        stddraw.line(i - 1, a[i - 1], i, a[i])

# -----------------------------------------------------------------------

def plotBars(a):
    """
    Plota os elementos do array a como barras.

    :param a: Lista de números a serem plotados.
    :returns: None
    """
    n = len(a)
    stddraw.setXscale(-1, n)
    for i in range(n):
        stddraw.filledRectangle(i - 0.25, 0.0, 0.5, a[i])

# -----------------------------------------------------------------------

def _main():
    """
    Função principal para testes.

    Lê um array de números e exibe estatísticas básicas (média, desvio padrão, mediana).

    :returns: None
    """
    import stdarray
    from stdio import writef

    a = stdarray.readFloat1D()
    writef("       min %7.3f\n", min(a))
    writef("       max %7.3f\n", max(a))
    writef("      mean %7.3f\n", mean(a))
    writef("   std dev %7.3f\n", stddev(a))
    writef("    median %7.3f\n", median(a))

if __name__ == "__main__":
    _main()

# -----------------------------------------------------------------------