import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from B_Spline import BSpline
from point import PointData
from mysound import sound

Fs = 10
pp = PointData()
pp.setStart(1.0)
pp.setEnd(2.0)
pp.setAnchors(0, 0.2, 2)
pp.setAnchors(1, 0.3, -1)
pp.setAnchors(2, 0.35, 6)
pp.setAnchors(3, 0.5, 4)
pp.setAnchors(4, 0.6, 0)
pp.insert(0.9, -10)
tmp = pp.getData()
line = BSpline().calc(tmp, sample=Fs)
x = tmp[:, 0]
y = tmp[:, 1]
sd = sound()
line2 = sd.soundGen(line, Durtime=1, Fstimes=Fs)


def FFT(Fs, data):
    L = len(data)  # 信号长度
    N = int(np.power(2, np.ceil(np.log2(L))))  # 下一个最近二次幂
    FFT_y1 = np.abs(fft(data, N)) / L * 2  # N点FFT 变化,但处于信号长度
    Fre = np.arange(int(N / 2)) * Fs / N  # 频率坐标
    FFT_y1 = FFT_y1[range(int(N / 2))]  # 取一半
    return Fre, FFT_y1


plt.subplot(2, 1, 1)
print(line2)
plt.plot(line2)
Fre, FFT_y1 = FFT(Fs, line2)
plt.subplot(2, 1, 2)
plt.plot(Fre, FFT_y1)
plt.grid()
plt.show()
