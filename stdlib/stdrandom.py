"""stdrandom.py.

O módulo stdrandom define funções relacionadas a números pseudo-aleatórios.

"""

import math
import random

# -----------------------------------------------------------------------

def seed(i=None):
    """
    Define a semente para o gerador de números aleatórios como hash(i), onde i é um inteiro.

    Se i for None, utiliza o tempo atual ou, conforme descrito na página de ajuda para random.seed(),
    "uma fonte de aleatoriedade específica do sistema operacional, se disponível".

    :param i: Inteiro usado como semente, ou None para comportamento padrão.
    :returns: None
    """
    random.seed(i)

# -----------------------------------------------------------------------

def uniform(hi):
    """
    Retorna um número inteiro escolhido uniformemente no intervalo [0, hi).

    :param hi: Limite superior (exclusivo) para o número aleatório.
    :returns: Um número inteiro aleatório.
    """
    return random.randrange(0, hi)

# -----------------------------------------------------------------------

def uniformInt(lo, hi):
    """
    Retorna um número inteiro escolhido uniformemente no intervalo [lo, hi).

    :param lo: Limite inferior (inclusivo) para o número aleatório.
    :param hi: Limite superior (exclusivo) para o número aleatório.
    :returns: Um número inteiro aleatório.
    """
    return random.randrange(lo, hi)

# -----------------------------------------------------------------------

def uniformFloat(lo, hi):
    """
    Retorna um número em ponto flutuante escolhido uniformemente no intervalo [lo, hi).

    :param lo: Limite inferior (inclusivo) para o número aleatório.
    :param hi: Limite superior (exclusivo) para o número aleatório.
    :returns: Um número em ponto flutuante aleatório.
    """
    return random.uniform(lo, hi)

# -----------------------------------------------------------------------

def bernoulli(p=0.5):
    """
    Retorna True com probabilidade p.

    :param p: Probabilidade de sucesso (0 <= p <= 1).
    :returns: True com probabilidade p, caso contrário False.
    """
    return random.random() < p

# -----------------------------------------------------------------------

def binomial(n, p=0.5):
    """
    Retorna o número de sucessos em n experimentos de Bernoulli, cada um com probabilidade de sucesso p.

    :param n: Número de experimentos.
    :param p: Probabilidade de sucesso em cada experimento (0 <= p <= 1).
    :returns: Número de sucessos em n experimentos.
    """
    heads = 0
    for i in range(n):
        if bernoulli(p):
            heads += 1
    return heads

# -----------------------------------------------------------------------

def gaussian(mean=0.0, stddev=1.0):
    """
    Retorna um número em ponto flutuante de acordo com uma distribuição Gaussiana padrão com média (mean)
    e desvio padrão (stddev) fornecidos.

    :param mean: Média da distribuição.
    :param stddev: Desvio padrão da distribuição.
    :returns: Um número em ponto flutuante da distribuição Gaussiana.
    """
    # Abordagem 1:
    # return random.gauss(mu, sigma)

    # Abordagem 2: Usa a forma polar da transformação de Box-Muller.
    x = uniformFloat(-1.0, 1.0)
    y = uniformFloat(-1.0, 1.0)
    r = x * x + y * y
    while (r >= 1) or (r == 0):
        x = uniformFloat(-1.0, 1.0)
        y = uniformFloat(-1.0, 1.0)
        r = x * x + y * y
    g = x * math.sqrt(-2 * math.log(r) / r)
    # Nota: x * math.sqrt(-2 * math.log(r) / r) é um número gaussiano independente.
    return mean + stddev * g

# -----------------------------------------------------------------------

def discrete(a):
    """
    Retorna um índice com base em uma distribuição discreta: i com probabilidade a[i].

    Pré-condição: os elementos do array a somam 1.

    :param a: Lista de probabilidades associadas a cada índice.
    :returns: Um índice baseado na distribuição fornecida.
    """
    r = uniformFloat(0.0, sum(a))
    subtotal = 0.0
    for i in range(len(a)):
        subtotal += a[i]
        if subtotal > r:
            return i

# -----------------------------------------------------------------------

def shuffle(a):
    """
    Embaralha os elementos do array a.

    :param a: Lista a ser embaralhada.
    :returns: None
    """
    random.shuffle(a)

# -----------------------------------------------------------------------

def exp(lambd):
    """
    Retorna um número em ponto flutuante de uma distribuição exponencial com taxa lambd.

    :param lambd: Taxa da distribuição exponencial (lambda > 0).
    :returns: Um número em ponto flutuante da distribuição exponencial.
    """
    return -math.log(1 - random.random()) / lambd

# -----------------------------------------------------------------------

def _main():
    """
    Função principal para testes.

    Gera e exibe valores baseados em diferentes distribuições e funções implementadas.

    :returns: None
    """
    import sys
    from stdio import writef, writeln

    seed(1)
    n = int(sys.argv[1])
    for i in range(n):
        writef(" %2d ", uniformInt(10, 100))
        writef("%8.5f ", uniformFloat(10.0, 99.0))
        writef("%5s ", bernoulli())
        writef("%5s ", binomial(100, 0.5))
        writef("%7.5f ", gaussian(9.0, 0.2))
        writef("%2d ", discrete([0.5, 0.3, 0.1, 0.1]))
        writeln()

if __name__ == "__main__":
    _main()

# -----------------------------------------------------------------------