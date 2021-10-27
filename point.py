import numpy as np


class EdgePoint():
    start = np.array([0.0, 0.0])
    end = np.array([1.0, 0.0])

    def setStart(self, y):
        self.start[1] = y

    def setEnd(self, y):
        self.end[1] = y


class AnchorPoint():
    anchors = np.array([[0.0, 0.0]] * 5)

    def setAnchors(self, index, x, y):
        self.anchors[index][0] = x
        self.anchors[index][1] = y

    def insert(self, x, y):
        l = 0
        r = len(self.anchors) - 1
        i = int(l + (r - l) / 2)
        if x > self.anchors[r][0]:
            self.anchors = np.insert(self.anchors, r+1, [x, y], axis=0)
            return
        elif x < self.anchors[l][0]:
            self.anchors = np.insert(self.anchors, l, [x, y], axis=0)
            return
        else:
            while l <= i < r:
                if self.anchors[i][0] <= x < self.anchors[i+1][0]:
                    break
                elif x > self.anchors[i+1][0]:
                    l = i + 1
                else:
                    r = i
                i = int(l + (r - l) / 2)
            self.anchors = np.insert(self.anchors, i+1, [x, y], axis=0)


class PointData(EdgePoint, AnchorPoint):

    def getData(self):
        tmp = [it for it in self.anchors]
        tmp.insert(0, self.start)
        tmp.append(self.end)
        return np.array(tmp)


if __name__ == '__main__':
    pp = PointData()
    pp.setStart(1)
    pp.setEnd(2)
    pp.setAnchors(0, 0.2, 2)
    pp.setAnchors(1, 0.3, -1)
    pp.setAnchors(2, 0.35, 6)
    pp.setAnchors(3, 0.5, 4)
    pp.setAnchors(4, 0.6, 0)
    pp.insert(0.9, 1)
    print(pp.getData())
