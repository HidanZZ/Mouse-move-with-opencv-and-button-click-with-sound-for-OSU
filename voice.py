import pyaudio
import numpy as np


class VoiceDetector:
    def __init__(self, chunk=600, rate=44100):
        self.chunk = chunk
        self.rate = rate

    def detect(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=self.rate, input=True,
                        frames_per_buffer=1024)
        data = np.frombuffer(stream.read(self.chunk), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        bars = int(peak / 800)
        return bars
