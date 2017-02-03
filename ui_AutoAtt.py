# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AutoAtt.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormAtt(object):
    def setupUi(self, FormAtt):
        FormAtt.setObjectName("FormAtt")
        FormAtt.setWindowModality(QtCore.Qt.NonModal)
        FormAtt.resize(600, 400)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(16)
        FormAtt.setFont(font)
        
        self.gridLayout_5 = QtWidgets.QGridLayout(FormAtt)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(FormAtt)
        
        
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        
        
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_Current1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Current1.setMaximum(63)
        self.spinBox_Current1.setSingleStep(1)
        self.spinBox_Current1.setProperty("value", 63)
        self.spinBox_Current1.setObjectName("spinBox_Current1")
        self.gridLayout_2.addWidget(self.spinBox_Current1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBox_Start1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Start1.setMaximum(63)
        self.spinBox_Start1.setObjectName("spinBox_Start1")
        self.gridLayout_2.addWidget(self.spinBox_Start1, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.spinBox_Finish1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Finish1.setMaximum(63)
        self.spinBox_Finish1.setProperty("value", 30)
        self.spinBox_Finish1.setObjectName("spinBox_Finish1")
        self.gridLayout_2.addWidget(self.spinBox_Finish1, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.spinBox_Step1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Step1.setMinimum(-10)
        self.spinBox_Step1.setMaximum(10)
        self.spinBox_Step1.setSingleStep(1)
        self.spinBox_Step1.setProperty("value", 3)
        self.spinBox_Step1.setObjectName("spinBox_Step1")
        self.gridLayout_2.addWidget(self.spinBox_Step1, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.spinBox_Interval1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Interval1.setProperty("value", 1)
        self.spinBox_Interval1.setObjectName("spinBox_Interval1")
        self.gridLayout_2.addWidget(self.spinBox_Interval1, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        
        
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 2, 1, 1)
        self.checkBox1 = QtWidgets.QCheckBox(self.groupBox)
        
        
        self.checkBox1.setFont(font)
        self.checkBox1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox1.setChecked(True)
        self.checkBox1.setObjectName("checkBox1")
        self.gridLayout_2.addWidget(self.checkBox1, 6, 0, 1, 3)
        self.spinBox_Repeat1 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_Repeat1.setProperty("value", 1)
        self.spinBox_Repeat1.setObjectName("spinBox_Repeat1")
        self.gridLayout_2.addWidget(self.spinBox_Repeat1, 5, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(FormAtt)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(FormAtt)
        
        
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 4, 2, 1, 1)
        self.checkBox2 = QtWidgets.QCheckBox(self.groupBox_2)
        
        
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.checkBox2.setFont(font)
        self.checkBox2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.checkBox2.setChecked(True)
        self.checkBox2.setObjectName("checkBox2")
        self.gridLayout_3.addWidget(self.checkBox2, 7, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.spinBox_Start2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Start2.setMaximum(63)
        self.spinBox_Start2.setObjectName("spinBox_Start2")
        self.gridLayout_3.addWidget(self.spinBox_Start2, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 2, 1, 1)
        self.spinBox_Repeat2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Repeat2.setProperty("value", 1)
        self.spinBox_Repeat2.setObjectName("spinBox_Repeat2")
        self.gridLayout_3.addWidget(self.spinBox_Repeat2, 6, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 2, 1, 1)
        self.spinBox_Step2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Step2.setMinimum(-10)
        self.spinBox_Step2.setMaximum(10)
        self.spinBox_Step2.setSingleStep(1)
        self.spinBox_Step2.setProperty("value", 3)
        self.spinBox_Step2.setObjectName("spinBox_Step2")
        self.gridLayout_3.addWidget(self.spinBox_Step2, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 2, 1, 1)
        self.spinBox_Finish2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Finish2.setMaximum(63)
        self.spinBox_Finish2.setProperty("value", 30)
        self.spinBox_Finish2.setObjectName("spinBox_Finish2")
        self.gridLayout_3.addWidget(self.spinBox_Finish2, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)
        self.spinBox_Interval2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Interval2.setProperty("value", 1)
        self.spinBox_Interval2.setObjectName("spinBox_Interval2")
        self.gridLayout_3.addWidget(self.spinBox_Interval2, 4, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)
        self.spinBox_Current2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Current2.setMaximum(63)
        self.spinBox_Current2.setProperty("value", 63)
        self.spinBox_Current2.setObjectName("spinBox_Current2")
        self.gridLayout_3.addWidget(self.spinBox_Current2, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        
        
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 6, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)



        self.groupBox_4 = QtWidgets.QGroupBox(FormAtt)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lcdNumber2 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber2.setDigitCount(2)
        self.lcdNumber2.setProperty("value", 63.0)
        self.lcdNumber2.setProperty("intValue", 63)
        self.lcdNumber2.setObjectName("lcdNumber2")
        self.gridLayout_4.addWidget(self.lcdNumber2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 2, 1, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(FormAtt)
        
    
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber1 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber1.setDigitCount(2)
        self.lcdNumber1.setProperty("value", 63.0)
        self.lcdNumber1.setProperty("intValue", 63)
        self.lcdNumber1.setObjectName("lcdNumber1")
        self.gridLayout.addWidget(self.lcdNumber1, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 2)

        self.pushButton_AutoSet = QtWidgets.QPushButton(FormAtt)
        font.setPointSize(24)
        self.pushButton_AutoSet.setFont(font)
        self.pushButton_AutoSet.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_AutoSet.setAutoDefault(False)
        self.pushButton_AutoSet.setDefault(False)
        self.pushButton_AutoSet.setFlat(False)
        self.pushButton_AutoSet.setObjectName("pushButton_AutoSet")
        self.gridLayout_5.addWidget(self.pushButton_AutoSet, 3, 0, 1, 1)
        self.pushButton_Close = QtWidgets.QPushButton(FormAtt)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.gridLayout_5.addWidget(self.pushButton_Close, 3, 1, 1, 2)

        self.retranslateUi(FormAtt)
        self.pushButton_Close.clicked.connect(FormAtt.close)
        self.spinBox_Current1.valueChanged['int'].connect(self.lcdNumber1.display)
        self.spinBox_Current2.valueChanged['int'].connect(self.lcdNumber2.display)
        QtCore.QMetaObject.connectSlotsByName(FormAtt)
        FormAtt.setTabOrder(self.spinBox_Current1, self.spinBox_Start1)
        FormAtt.setTabOrder(self.spinBox_Start1, self.spinBox_Finish1)
        FormAtt.setTabOrder(self.spinBox_Finish1, self.spinBox_Step1)
        FormAtt.setTabOrder(self.spinBox_Step1, self.spinBox_Interval1)
        FormAtt.setTabOrder(self.spinBox_Interval1, self.spinBox_Current2)
        FormAtt.setTabOrder(self.spinBox_Current2, self.spinBox_Start2)
        FormAtt.setTabOrder(self.spinBox_Start2, self.spinBox_Finish2)
        FormAtt.setTabOrder(self.spinBox_Finish2, self.spinBox_Step2)
        FormAtt.setTabOrder(self.spinBox_Step2, self.spinBox_Interval2)

    def retranslateUi(self, FormAtt):
        _translate = QtCore.QCoreApplication.translate
        FormAtt.setWindowTitle(_translate("FormAtt", "Attenuator"))
        self.groupBox.setTitle(_translate("FormAtt", "Attenuator-1"))
        self.label_21.setText(_translate("FormAtt", "Repeat:"))
        self.label.setText(_translate("FormAtt", "Current:"))
        self.label_2.setText(_translate("FormAtt", "dB"))
        self.label_3.setText(_translate("FormAtt", "Start:"))
        self.label_7.setText(_translate("FormAtt", "dB"))
        self.label_4.setText(_translate("FormAtt", "Finish:"))
        self.label_8.setText(_translate("FormAtt", "dB"))
        self.label_5.setText(_translate("FormAtt", "Step:"))
        self.label_9.setText(_translate("FormAtt", "dB"))
        self.label_6.setText(_translate("FormAtt", "Interval time:"))
        self.label_10.setText(_translate("FormAtt", "s"))
        self.checkBox1.setText(_translate("FormAtt", "Auto set attenuator-1 value"))
        self.groupBox_2.setTitle(_translate("FormAtt", "Attenuator-2"))
        self.label_20.setText(_translate("FormAtt", "s"))
        self.checkBox2.setText(_translate("FormAtt", "Auto set attenuator-2 value"))
        self.label_12.setText(_translate("FormAtt", "dB"))
        self.label_11.setText(_translate("FormAtt", "Current:"))
        self.label_15.setText(_translate("FormAtt", "Finish:"))
        self.label_16.setText(_translate("FormAtt", "dB"))
        self.label_14.setText(_translate("FormAtt", "dB"))
        self.label_18.setText(_translate("FormAtt", "dB"))
        self.label_13.setText(_translate("FormAtt", "Start:"))
        self.label_17.setText(_translate("FormAtt", "Step:"))
        self.label_19.setText(_translate("FormAtt", "Interval time:"))
        self.label_22.setText(_translate("FormAtt", "Repeat:"))
        self.pushButton_AutoSet.setText(_translate("FormAtt", "Auto Set Attenuator"))
        self.pushButton_AutoSet.setShortcut(_translate("FormAtt", "Return"))
        self.pushButton_Close.setText(_translate("FormAtt", "&Close"))
        self.groupBox_4.setTitle(_translate("FormAtt", "Attenuator-2"))
        self.groupBox_3.setTitle(_translate("FormAtt", "Attenuator-1"))

