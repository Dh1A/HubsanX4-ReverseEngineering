# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dhia\Desktop\drone_gui\drone.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("droneV1.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.up = QtGui.QLCDNumber(self.centralwidget)
        self.up.setGeometry(QtCore.QRect(30, 380, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PMincho"))
        self.up.setFont(font)
        self.up.setAutoFillBackground(True)
        self.up.setInputMethodHints(QtCore.Qt.ImhNone)
        self.up.setFrameShape(QtGui.QFrame.NoFrame)
        self.up.setFrameShadow(QtGui.QFrame.Plain)
        self.up.setMidLineWidth(1)
        self.up.setSmallDecimalPoint(False)
        self.up.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.up.setProperty("intValue", 0)
        self.up.setObjectName(_fromUtf8("up"))
        self.down = QtGui.QLCDNumber(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(30, 420, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PMincho"))
        self.down.setFont(font)
        self.down.setAutoFillBackground(True)
        self.down.setInputMethodHints(QtCore.Qt.ImhNone)
        self.down.setFrameShape(QtGui.QFrame.NoFrame)
        self.down.setFrameShadow(QtGui.QFrame.Plain)
        self.down.setMidLineWidth(1)
        self.down.setSmallDecimalPoint(False)
        self.down.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.down.setObjectName(_fromUtf8("down"))
        self.left = QtGui.QLCDNumber(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(630, 410, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PMincho"))
        self.left.setFont(font)
        self.left.setAutoFillBackground(True)
        self.left.setInputMethodHints(QtCore.Qt.ImhNone)
        self.left.setFrameShape(QtGui.QFrame.NoFrame)
        self.left.setFrameShadow(QtGui.QFrame.Plain)
        self.left.setMidLineWidth(1)
        self.left.setSmallDecimalPoint(False)
        self.left.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.left.setObjectName(_fromUtf8("left"))
        self.right = QtGui.QLCDNumber(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(630, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PMincho"))
        self.right.setFont(font)
        self.right.setAutoFillBackground(True)
        self.right.setInputMethodHints(QtCore.Qt.ImhNone)
        self.right.setFrameShape(QtGui.QFrame.NoFrame)
        self.right.setFrameShadow(QtGui.QFrame.Plain)
        self.right.setMidLineWidth(1)
        self.right.setSmallDecimalPoint(False)
        self.right.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.right.setProperty("intValue", 0)
        self.right.setObjectName(_fromUtf8("right"))
        self.upp = QtGui.QPushButton(self.centralwidget)
        self.upp.setGeometry(QtCore.QRect(66, 82, 111, 81))
        self.upp.setText(_fromUtf8(""))
        self.upp.setFlat(True)
        self.upp.setObjectName(_fromUtf8("upp"))
        self.upm = QtGui.QPushButton(self.centralwidget)
        self.upm.setGeometry(QtCore.QRect(70, 280, 111, 81))
        self.upm.setText(_fromUtf8(""))
        self.upm.setFlat(True)
        self.upm.setObjectName(_fromUtf8("upm"))
        self.downp = QtGui.QPushButton(self.centralwidget)
        self.downp.setGeometry(QtCore.QRect(160, 180, 111, 81))
        self.downp.setText(_fromUtf8(""))
        self.downp.setFlat(True)
        self.downp.setObjectName(_fromUtf8("downp"))
        self.downm = QtGui.QPushButton(self.centralwidget)
        self.downm.setGeometry(QtCore.QRect(0, 180, 111, 81))
        self.downm.setText(_fromUtf8(""))
        self.downm.setFlat(True)
        self.downm.setObjectName(_fromUtf8("downm"))
        self.leftp = QtGui.QPushButton(self.centralwidget)
        self.leftp.setGeometry(QtCore.QRect(510, 180, 111, 81))
        self.leftp.setText(_fromUtf8(""))
        self.leftp.setFlat(True)
        self.leftp.setObjectName(_fromUtf8("leftp"))
        self.leftm = QtGui.QPushButton(self.centralwidget)
        self.leftm.setGeometry(QtCore.QRect(720, 180, 111, 81))
        self.leftm.setText(_fromUtf8(""))
        self.leftm.setFlat(True)
        self.leftm.setObjectName(_fromUtf8("leftm"))
        self.rightp = QtGui.QPushButton(self.centralwidget)
        self.rightp.setGeometry(QtCore.QRect(620, 100, 111, 81))
        self.rightp.setText(_fromUtf8(""))
        self.rightp.setFlat(True)
        self.rightp.setObjectName(_fromUtf8("rightp"))
        self.rightm = QtGui.QPushButton(self.centralwidget)
        self.rightm.setGeometry(QtCore.QRect(620, 260, 111, 81))
        self.rightm.setText(_fromUtf8(""))
        self.rightm.setFlat(True)
        self.rightm.setObjectName(_fromUtf8("rightm"))
        self.info = QtGui.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(286, 412, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nyala"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(65)
        self.info.setFont(font)
        self.info.setObjectName(_fromUtf8("info"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.info.setText(_translate("MainWindow", "TextLabel", None))

