from mysound import sound
from MyCanvas import MyFigureCanvas
import numpy as np
from scipy import fft


def FFT(Fs, data):
    L = len(data)  # 信号长度
    N = int(np.power(2, np.ceil(np.log2(L))))  # 下一个最近二次幂
    FFT_y1 = np.abs(fft(data, N)) / L * 2  # N点FFT 变化,但处于信号长度
    Fre = np.arange(int(N / 2)) * Fs / N  # 频率坐标
    FFT_y1 = FFT_y1[range(int(N / 2))]  # 取一半
    return Fre, FFT_y1


class MathCompound:
    def __init__(self, Durtime, Fs, Fre):
        self.Durtime = Durtime
        self.Fs = Fs
        self.Fre = Fre
        # initialized canvas
        self.plt = MyFigureCanvas()
        # initialized sound ctrl
        self.sd = sound()
        # initialized canvas

    def setFre(self, f):
        self.Fre = f
        self.sd.setFre(f)

    def setFs(self, fs):
        self.Fs = fs
        self.sd.setFs(fs)

    def FreDominCalc(self):
        # regenerate signal
        self.sd.soundGen(self.plt.GetShape(),
                         Durtime=self.Durtime,
                         Fstimes=int(self.Fs/self.Fre))
        signal = self.sd.GetSignal()
        fre, f_signal = FFT(self.sd.fs, signal)
        return fre, f_signal
