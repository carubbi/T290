# baseado em https://introcs.cs.princeton.edu/python/code/stdlib-python.zip baixado em dezembro de 2017

"""stdaudio.py.

O módulo stdaudio define funções relacionadas à manipulação de áudio.

"""

import sys
import numpy
import pygame
from stdio import writeln

# -----------------------------------------------------------------------

_SAMPLES_PER_SECOND = 44100  # Taxa de amostragem
_SAMPLE_SIZE = -16  # Cada amostra é um inteiro de 16 bits com sinal
_CHANNEL_COUNT = 1  # 1 => mono, 2 => stereo
_AUDIO_BUFFER_SIZE = 1024  # Tamanho do buffer de áudio em amostras
_CHECK_RATE = 44100  # Frequência para verificar a fila

_myBuffer = []  # Buffer interno para amostras de som
_MY_BUFFER_MAX_LENGTH = 4096  # Comprimento máximo do buffer (determinado experimentalmente)

# -----------------------------------------------------------------------

def wait():
    """Aguarda a fila de áudio ficar vazia.

    Informalmente, aguarda até que o som atual termine de tocar.
    """
    global _channel
    clock = pygame.time.Clock()
    while _channel.get_queue() is not None:
        clock.tick(_CHECK_RATE)


# -----------------------------------------------------------------------

def playSample(s):
    """Reproduz uma amostra de som.

    :param s: A amostra de som a ser reproduzida.
    """
    global _myBuffer
    global _channel

    _myBuffer.append(s)

    if len(_myBuffer) > _MY_BUFFER_MAX_LENGTH:
        temp = []
        for sample in _myBuffer:
            temp.append(numpy.int16(sample * float(0x7FFF)))  # Converte para 16 bits
        samples = numpy.array(temp, numpy.int16)
        sound = pygame.sndarray.make_sound(samples)
        wait()
        _channel.queue(sound)
        _myBuffer = []  # Limpa o buffer


# -----------------------------------------------------------------------

def playSamples(a):
    """Reproduz todas as amostras de som em um array.

    :param a: Array de amostras de som a serem reproduzidas.
    """
    for sample in a:
        playSample(sample)


# -----------------------------------------------------------------------

def playArray(a):
    """[Obsoleto] Reproduz todas as amostras em um array.

    Comportamento equivalente a stdaudio.playSamples().

    :param a: Array de amostras de som a serem reproduzidas.
    """
    playSamples(a)


# -----------------------------------------------------------------------

def playFile(f):
    """Reproduz todas as amostras de som do arquivo especificado.

    :param f: Nome do arquivo (sem extensão .wav).
    """
    a = read(f)
    playSamples(a)


# -----------------------------------------------------------------------

def save(f, a):
    """Salva todas as amostras em um arquivo WAV.

    :param f: Nome do arquivo (sem extensão .wav).
    :param a: Array de amostras de som a serem salvas.
    """
    import wave

    fileName = f + ".wav"
    temp = []
    for sample in a:
        temp.append(int(sample * float(0x7FFF)))  # Converte para 16 bits
    samples = numpy.array(temp, numpy.int16)

    file = wave.open(fileName, "w")
    file.setnchannels(_CHANNEL_COUNT)
    file.setsampwidth(2)  # 2 bytes por amostra
    file.setframerate(_SAMPLES_PER_SECOND)
    file.setnframes(len(samples))
    file.setcomptype("NONE", "descrip")  # Sem compressão
    file.writeframes(samples.tobytes())
    file.close()


# -----------------------------------------------------------------------

def read(f):
    """Lê todas as amostras do arquivo WAV especificado.

    :param f: Nome do arquivo (sem extensão .wav).
    :returns: Array com as amostras de som.
    """
    fileName = f + ".wav"
    sound = pygame.mixer.Sound(fileName)
    samples = pygame.sndarray.samples(sound)
    temp = []
    for i in range(len(samples)):
        temp.append(float(samples[i]) / float(0x7FFF))  # Normaliza para [-1, 1]
    return temp


# -----------------------------------------------------------------------
# Inicializa o PyGame para manipular áudio
# -----------------------------------------------------------------------

try:
    pygame.mixer.init(
        _SAMPLES_PER_SECOND, _SAMPLE_SIZE, _CHANNEL_COUNT, _AUDIO_BUFFER_SIZE
    )
    _channel = pygame.mixer.Channel(0)  # Canal de áudio
except pygame.error:
    writeln("Não foi possível inicializar o PyGame")
    sys.exit(1)


# -----------------------------------------------------------------------

def _createTextAudioFile():
    """Cria um arquivo de texto com dados de áudio para teste."""
    notes = [
        7,
        0.270,
        5,
        0.090,
        3,
        0.180,
        5,
        0.180,
        7,
        0.180,
        6,
        0.180,
        7,
        0.180,
        3,
        0.180,
        5,
        0.180,
        5,
        0.180,
        5,
        0.180,
        5,
        0.900,
        5,
        0.325,
        3,
        0.125,
        2,
        0.180,
        3,
        0.180,
        5,
        0.180,
        4,
        0.180,
        5,
        0.180,
        2,
        0.180,
        3,
        0.180,
        3,
        0.180,
        3,
        0.180,
        3,
        0.900,
    ]

    from stdlib import outstream

    outStream = outstream.OutStream("looney.txt")
    for note in notes:
        outStream.writeln(note)


# -----------------------------------------------------------------------
# Função principal para testes
# -----------------------------------------------------------------------

def _main():
    """Executa testes para as funções do módulo stdaudio."""
    import math
    import os
    from stdlib import instream

    _createTextAudioFile()

    writeln("Criando e tocando em pequenos pedaços...")
    sps = _SAMPLES_PER_SECOND
    inStream = instream.InStream("looney.txt")
    while not inStream.isEmpty():
        pitch = inStream.readInt()
        duration = inStream.readFloat()
        hz = 440 * math.pow(2, pitch / 12.0)
        N = int(sps * duration)
        notes = []
        for i in range(N + 1):
            notes.append(math.sin(2 * math.pi * i * hz / sps))
        playSamples(notes)
    wait()

    writeln("Criando e tocando em um único grande pedaço...")
    sps = _SAMPLES_PER_SECOND
    notes = []
    inStream = instream.InStream("looney.txt")
    while not inStream.isEmpty():
        pitch = inStream.readInt()
        duration = inStream.readFloat()
        hz = 440 * math.pow(2, pitch / 12.0)
        N = int(sps * duration)
        for i in range(N + 1):
            notes.append(math.sin(2 * math.pi * i * hz / sps))
    playSamples(notes)
    wait()

    writeln("Salvando...")
    save("looney", notes)

    writeln("Lendo...")
    notes = read("looney")

    writeln("Tocando um array...")
    playSamples(notes)
    wait()

    writeln("Tocando um arquivo...")
    playFile("looney")
    wait()

    os.remove("looney.wav")
    os.remove("looney.txt")


if __name__ == "__main__":
    _main()