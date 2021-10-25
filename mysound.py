import numpy as np
import pyaudio

class sound:
    fs = 0.0
    Fre = 440.0
    sd = []

    def soundGen(self, sample, time, fs):
        self.fs = fs
        # x = sample[0]
        y = sample[1]
        # y.tobytes()
        T = int(time * fs / len(y))
        self.sd = []
        for i in range(T):
            self.sd.append(y)

        self.sd = np.array(self.sd).tobytes()

    def setVolume(self, vloume):
        self.sd *= vloume

    def setFre(self, f):
        self.Fre = f

    def play(self):
        p = pyaudio.PyAudio()
        stream = p.open(channels=1, format=pyaudio.paInt32, rate=fs, output=True)
        stream.write(self.sd)
        stream.stop_stream()
        stream.close()

if __name__ == '__main__':
    x = np.linspace(0, 2*np.pi, 100)
    y = 20 * np.square(x)
    y_box = []
    for i in range(100):
        y_box.append(y)
    y_box = np.array(y_box).tobytes()
    f = 440
    p = pyaudio.PyAudio()
    stream = p.open(channels=1, format=pyaudio.paInt32, rate=100*440, output=True)
    stream.write(y_box)
    stream.stop_stream()
    stream.close()
