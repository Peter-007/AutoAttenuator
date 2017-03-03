#!/usr/bin/env python

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import time, threading

from ui_AutoAtt import Ui_FormAtt


from Attenuator import ATT

class FormAtt(QWidget):
    def __init__(self, parent=None):
        super(FormAtt, self).__init__(parent)

        self.ui = Ui_FormAtt()
        self.ui.setupUi(self)

        self.att1 = ATT(1)
        self.att2 = ATT(2)

    # 创建循环配置的衰减值列表,如：[0,3,6,9,6,3]
    # Start: 开始衰减值
    # Finish:终止衰减值
    # Step: 步进值
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

    # 根据用户在界面配置的开始／终止／步进／时间间隔／重复次数的参数值自动周期性的改变1号衰减器模块的值
    def autoSetAtt1(self):
        if self.ui.checkBox1.isChecked():
            # 改变界面控件状态，使得用户不能在自动控制衰减器模块期间，进行其他操作
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

            if threading.active_count() == self.iThreadCount + 1:  #如果两个线程结束，打开相应按钮的使能
                self.ui.pushButton_AutoSet.setEnabled(True)
                self.ui.pushButton_Close.setEnabled(True)

    # 根据用户在界面配置的开始／终止／步进／时间间隔／重复次数的参数值自动周期性的改变2号衰减器模块的值
    def autoSetAtt2(self):
        if self.ui.checkBox1.isChecked():
            # 改变界面控件状态，使得用户不能在自动控制衰减器模块期间，进行其他操作
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

            if threading.active_count() == self.iThreadCount + 1:     #如果两个线程结束，打开相应按钮的使能
                self.ui.pushButton_AutoSet.setEnabled(True)
                self.ui.pushButton_Close.setEnabled(True)

    # 定义一个Slot，实时的改变1号衰减器模块的值
    @pyqtSlot(int)
    def on_spinBox_Current1_valueChanged(self, value):
        print('Set Attenuator-1 value: %d dB' % value)
        # self.att1.SetAtt(value)

    # 定义一个Slot， 实时的改变2号衰减器模块的值
    @pyqtSlot(int)
    def on_spinBox_Current2_valueChanged(self, value):
        print('Set Attenuator-2 value: %d dB' % value)
        # self.att2.SetAtt(value)

    #创建两个线程实现两个衰减器模块值周期性的自动改变衰减值
    @pyqtSlot()
    def on_pushButton_AutoSet_clicked(self):
        self.iThreadCount = threading.activeCount()
        print('threadcount=%d' % self.iThreadCount)
        t1 = threading.Thread(target=self.autoSetAtt1)
        t2 = threading.Thread(target=self.autoSetAtt2)
        t1.start()
        t2.start()
        self.iThreadCount = threading.activeCount()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    formAtt = FormAtt()
    formAtt.show()

    sys.exit(app.exec_())
