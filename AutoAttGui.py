#!/usr/bin/env python

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import time, threading

from ui_AutoAtt import Ui_FormAtt


# from Attenuator import ATT

class FormAtt(QWidget):
    def __init__(self, parent=None):
        super(FormAtt, self).__init__(parent)

        self.ui = Ui_FormAtt()
        self.ui.setupUi(self)

        # self.att1 = ATT(1)
        # self.att2 = ATT(2)

    def CreateAttList(self, Start, Finish, Step):
        lst1 = list(range(Start, Finish + int(Step / abs(Step)), Step))
        lstResult = []
        lstResult = lstResult + lst1
        lst1.pop(0)
        lst1.pop(-1)
        lst1.reverse()
        lstResult = lstResult + lst1
        print(lstResult)
        return lstResult

    def autoSetAtt1(self):
        if self.ui.checkBox1.isChecked():
            self.ui.pushButton_AutoSet.setEnabled(False)
            self.ui.pushButton_Close.setEnabled(False)
            self.ui.spinBox_Current1.setEnabled(False)

            iStart = self.ui.spinBox_Start1.value()
            iFinish = self.ui.spinBox_Finish1.value()
            iStep = self.ui.spinBox_Step1.value()
            iInterval = self.ui.spinBox_Interval1.value()
            iRepeat = self.ui.spinBox_Repeat1.value()

            for i in range(iRepeat):
                for j in self.CreateAttList(iStart, iFinish, iStep):
                    self.ui.spinBox_Current1.setValue(j)
                    time.sleep(iInterval)

            self.ui.spinBox_Current1.setValue(iStart)
            self.ui.spinBox_Current1.setEnabled(True)

            if threading.active_count() == self.iThreadCount + 1:
                self.ui.pushButton_AutoSet.setEnabled(True)
                self.ui.pushButton_Close.setEnabled(True)

    def autoSetAtt2(self):
        if self.ui.checkBox1.isChecked():
            self.ui.pushButton_AutoSet.setEnabled(False)
            self.ui.pushButton_Close.setEnabled(False)
            self.ui.spinBox_Current1.setEnabled(False)

            iStart = self.ui.spinBox_Start2.value()
            iFinish = self.ui.spinBox_Finish2.value()
            iStep = self.ui.spinBox_Step2.value()
            iInterval = self.ui.spinBox_Interval2.value()
            iRepeat = self.ui.spinBox_Repeat2.value()

            for i in range(iRepeat):
                for j in self.CreateAttList(iStart, iFinish, iStep):
                    self.ui.spinBox_Current2.setValue(j)
                    time.sleep(iInterval)

            self.ui.spinBox_Current2.setValue(iStart)
            self.ui.spinBox_Current2.setEnabled(True)

            if threading.active_count() == self.iThreadCount + 1:
                self.ui.pushButton_AutoSet.setEnabled(True)
                self.ui.pushButton_Close.setEnabled(True)

    @pyqtSlot(int)
    def on_spinBox_Current1_valueChanged(self, value):
        print('Set Attenuator-1 value: %d dB' % value)
        # self.att1.SetAtt(value)

    @pyqtSlot(int)
    def on_spinBox_Current2_valueChanged(self, value):
        print('Set Attenuator-2 value: %d dB' % value)
        # self.att2.SetAtt(value)

    @pyqtSlot()
    def on_pushButton_AutoSet_clicked(self):
        self.iThreadCount = threading.activeCount()
        print('threadcount=%d' % self.iThreadCount)
        t1 = threading.Thread(target=self.autoSetAtt1)
        t2 = threading.Thread(target=self.autoSetAtt2)
        t1.start()
        t2.start()
        # self.iThreadCount = threading.activeCount()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    formAtt = FormAtt()
    formAtt.show()

    sys.exit(app.exec_())
