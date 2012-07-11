# -*- coding: utf-8 *-*
import alsaaudio
import numpy as np


class Capture(object):
    def __init__(self, cant_samples=800, fs=44100):
        self.cap = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
        self.cap.setchannels(1)
        self.cap.setperiodsize(cant_samples)
        self.cap.setrate(44100)
        print self.cap.dumpinfo()

    def get(self):
        data = self.cap.read()[1]
        return np.fromstring(data, dtype=np.int16)
