import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt


class BSpline:

    def calc(self, point, k=3, sample=100):
        """
        :param point: ctrl point
        :param k: degrees
        :param sample: Length of the output.
        :return: B Spline curve witch is a list contain sequence of x,y
        """
        ctr = np.array(point)
        x = ctr[:, 0]
        y = ctr[:, 1]
        l = len(x)
        t = np.linspace(0, 1, l - k+1, endpoint=True)
        t = np.append([0]*k, t)
        t = np.append(t, [1]*k)

        tck = [t, [x, y], k]
        u3 = np.linspace(0, 1, sample, endpoint=True)
        out = interpolate.splev(u3, tck)
        return out

