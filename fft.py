# -*- coding: utf-8 *-*
import numpy as np
from numpy.fft import rfft, fftfreq
from scipy.signal import blackmanharris


class FFT(object):
    u"""
    Is a "helper" for FFT, windowed and axis x scale to frequency values
    """
    def __init__(self, fs=44100, window=blackmanharris, data=None):
        self.window= window
        self.fs = fs
        self.data = data

    def set_data(self, data):
        self.data = data

    def calculate(self):
        data = self.data * blackmanharris(self.data.size)
        finfo = np.abs(rfft(data))
        xvals = fftfreq(self.data.size, d=(1.0 / self.fs))
        xvals = xvals[:xvals.size / 8]
        if finfo.size != xvals.size:
            finfo = finfo[:xvals.size]
            xvals = xvals[:finfo.size]
        return xvals, finfo


if __name__ == "__main__":
    from matplotlib import pyplot
    fs = 44100
    fft = FFT(fs)
    fft.set_data(np.sin(2 * np.pi * 10000 / fs * np.array(range(800))))
    freq, amplitude = fft.calculate()
    pyplot.plot(freq, amplitude)
    pyplot.show()
