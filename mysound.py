import numpy as np
import pyaudio


class sound:
    fs = 0
    Fre = 440
    sd = []

    def soundGen(self, sample, Durtime, Fstimes):
        """
        :param sample: base sample signal
        :param Durtime: Duration time
        :param Fstimes: proportion between Frequency sample  and frequency
        :return: output signal which is a sequence of repetitive sample
        """
        self.fs = self.Fre * Fstimes
        # x = sample[0]
        y = sample[1]
        T = int(Durtime * self.fs / (4 * len(y)))
        # 这里*4是因为在播放的时候转成bytes流播放，每一个数据转成32位字节，正好是1到4
        self.sd = []
        for i in range(T):
            self.sd.extend(y)
        self.sd = np.array(self.sd)

    def GetSignal(self):
        return self.sd

    def setVolume(self, vloume):
        pass

    def setFre(self, f):
        self.Fre = f

    def setFs(self, fs):
        self.fs = fs

    def play(self):
        p = pyaudio.PyAudio()
        stream = p.open(channels=1,
                        format=pyaudio.paInt32,
                        output=True,
                        rate=self.fs)
        # 这里需要将float转成bytes类型输出到缓冲流流
        stream.write(self.sd.tobytes())
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
    stream = p.open(channels=1,
                    format=pyaudio.paInt32,
                    rate=100*440,
                    output=True)
    stream.write(y_box)
    stream.stop_stream()
    stream.close()
