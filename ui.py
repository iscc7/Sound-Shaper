import sys
import numpy as np
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import matplotlib

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from point import PointData
from B_Spline import BSpline


class MyFigureCanvas(FigureCanvas):

    showverts = True
    epsilon = 10
    def __init__(self):
        # create a canvas

        fig = plt.figure()
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)
        # canvas initialized

        # new a "control points" instance
        self.CtrlPoints = PointData()
        self._ind = None # initialize index of ctrl point
        # new a B-Spline line
        self.B_Spline_line = self._spline_calc(self.CtrlPoints.getData())
        self.FigInit()
        # initialize poly
        poly = Polygon(self.xy, animated=True, closed=False)
        self.poly = poly
        self.axes.add_patch(poly)
        self.mpl_connect('button_press_event', self.button_press_callback)
        self.mpl_connect('button_release_event', self.button_release_callback)
        self.mpl_connect('motion_notify_event', self.motion_notify_callback)



    def FigInit(self):
        import random
        for i in range(5):
            x = 0.8 * (0.2 + i/5.0)
            self.CtrlPoints.setAnchors(i, x, random.random())
        self._draw_CtrlPoints()
        self._draw_curve()
        self.draw()

    def _spline_calc(self, CtrlPoints):
        return BSpline().calc(CtrlPoints)

    def _draw_CtrlPoints(self):
        self.xy = self.CtrlPoints.getData()
        x = self.xy[:, 0]
        y = self.xy[:, 1]
        self.axes.plot(x, y, 'o')

    def _draw_curve(self):
        ctrl = self.CtrlPoints.getData()
        self.B_Spline_line = self._spline_calc(ctrl)
        self.axes.plot(self.B_Spline_line[0], self.B_Spline_line[1])

    def FigReGen(self):
        self.axes.clear()
        self._draw_CtrlPoints()
        self._draw_curve()
        self.draw()

    def get_ind_under_point(self, event):
        # 计算鼠标点是否在某个点的范围内
        xy = np.asarray(self.poly.xy)
        xyt = self.poly.get_transform().transform(xy)
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x) ** 2 + (yt - event.y) ** 2)
        indseq = np.nonzero(np.equal(d, np.amin(d)))[0]
        ind = indseq[0]

        if d[ind] >= self.epsilon:
            ind = None
        return ind

    def button_press_callback(self, event):
        '鼠标按下事件处理'
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        self._ind = self.get_ind_under_point(event)

    def button_release_callback(self, event):
        '鼠标松开事件处理'
        if not self.showverts:
            return
        if event.button != 1:
            return
        self._ind = None

    def motion_notify_callback(self, event):
        '鼠标移动事件处理'
        if not self.showverts:
            return
        if self._ind is None:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        # get x and y
        x, y = event.xdata, event.ydata
        # update x and y
        self.poly.xy[self._ind] = x, y
        if self._ind == 0:
            self.CtrlPoints.setStart(y)
        elif self._ind == self.CtrlPoints.size():
            self.CtrlPoints.setEnd(y)
        else:
            self.CtrlPoints.setAnchors(self._ind - 1, x, y)
        # refresh figure
        self.FigReGen()

class MainWindow():
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("./mainUI.ui")
        self.initUI()

    def initUI(self):
        self.plt = MyFigureCanvas()
        self.ui.horizontalLayout.addWidget(self.plt)
        # self.ui.play.clicked.connect(self.plt.FigReGen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.ui.show()
    sys.exit(app.exec_())