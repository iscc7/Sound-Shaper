import numpy as np


class EndPoint():
    start = np.array([0.0, 0.0])
    end = np.array([1.0, 0.0])

    def setStart(self, y):
        self.start[1] = y

    def setEnd(self, y):
        self.end[1] = y


class AnchorPoint():
    anchors = np.array([[0.0, 0.0]]*5)

    def setAnchors(self, index, x, y):
        self.anchors[index][0] = x
        self.anchors[index][1] = y


class PointData(EndPoint, AnchorPoint):

    def getData(self):
        tmp = [it for it in self.anchors]
        tmp.insert(0, self.start)
        tmp.append(self.end)
        return np.array(tmp)

if __name__ == '__main__':
    pp = PointData()
    pp.setStart(1)
    pp.setEnd(2)
    pp.setAnchors(0, 1, 2)
    print(pp.getData())