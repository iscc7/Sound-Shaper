from B_Spline import BSpline
from point import PointData
from matplotlib import pyplot as plt
from mysound import sound

pp = PointData()
pp.setStart(1.0)
pp.setEnd(2.0)
pp.setAnchors(0, 0.2, 2)
pp.setAnchors(1, 0.3, -1)
pp.setAnchors(2, 0.35, 6)
pp.setAnchors(3, 0.5, 4)
pp.setAnchors(4, 0.6, 0)
tmp = pp.getData()
line = BSpline().calc(tmp, sample=100)
x = tmp[:, 0]
y = tmp[:, 1]


sd = sound()
sd.soundGen(line, fs=100*440, time=1)
sd.play()

plt.plot(line[0], line[1])
plt.plot(x, y, '--', marker='o')
plt.show()
