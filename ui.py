import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox
import MidLayer


class MainWindow:

    Durtime = 1
    Fre = 440
    Fs = 10 * Fre

    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("./mainUI.ui")
        self.com = MidLayer.MathCompound(self.Durtime,
                                         Fre=self.Fre,
                                         Fs=self.Fs)

        self.initUI()
        self.EventsBindingInit()

    def initUI(self):
        self.ui.horizontalLayout.addWidget(self.com.plt)
        # self.ui.play.clicked.connect(self.plt.FigReGen)
        self.ui.FreEdit.setPlaceholderText("set frequency here")

    def EventsBindingInit(self):
        self.ui.play.clicked.connect(self.__soundPlayHandle)
        self.ui.FreEdit.textChanged.connect(self.__FreEditHandle)
        self.ui.DominSelection.currentIndexChanged.connect(self.__DominSelectionHandle)

    def __soundPlayHandle(self):
        shape = self.com.plt.GetShape()
        self.com.sd.soundGen(shape, self.Durtime, 100)
        self.com.sd.play()

    def __FreEditHandle(self):
        edit = self.ui.FreEdit.text()
        if edit == '':
            return
        try:
            f = int(edit)
            if f < 0 or f > 24000:
                QMessageBox.warning(self.ui, '小可爱', '超出听觉极限了哦！')
                return
            self.Fre = f
            self.com.setFre(f)

        except ValueError:
            QMessageBox.warning(self.ui, '警告', '输入的并不是很对')

    def __DominSelectionHandle(self):
        dom = self.ui.DominSelection.currentText()
        if dom == 'Time Domin':
            print('time dom selected')
            self.com.plt.TimFigGen()

        elif dom == 'Frequency Domin':
            print('fre dom time dom selected')
            f, f_signal = self.com.FreDominCalc()
            self.com.plt.FreFigGen(fre=f,
                                   f_signal=f_signal)

        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.ui.show()
    sys.exit(app.exec_())