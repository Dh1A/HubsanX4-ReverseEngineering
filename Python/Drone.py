import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import dronev1

import time

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)






class MainG (QtGui.QMainWindow ,dronev1.Ui_MainWindow):



    def __init__(self, parent = None ):




        super(MainG,self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()


        self.info.setText("Recherche de drone..")
        self.upp.clicked.connect( self.btnupp)
        self.upm.clicked.connect(self.btnupm)
        self.downp.clicked.connect(self.btndp)
        self.downm.clicked.connect(self.btndm)
        self.rightm.clicked.connect(self.btnrm)
        self.rightp.clicked.connect(self.btnrp)
        self.leftp.clicked.connect(self.btnlp)
        self.leftm.clicked.connect(self.btnlm)







    def btnupp (self):
        a = self.up.intValue()
        a = a+1
        self.up.display(a)
        message = list("Throttle"+str(a)+"")
        while len(message) < 32:
            message.append(0)
        radio.write(message)




    def btnupm (self):
        radio.stopListening()
        a = self.up.intValue()
        a = a-1
        self.up.display(a)
        message = list("Throttle" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)


    def btnrp (self):
        radio.stopListening()
        a = self.right.intValue()
        a = a+1
        self.right.display(a)
        message = list("Pitch" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)

    def btnrm (self):
        radio.stopListening()
        a = self.right.intValue()
        a = a-1
        self.right.display(a)
        message = list("Pitch" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)

    def btnlp (self):
        radio.stopListening()
        a = self.left.intValue()
        a = a+1
        self.left.display(a)
        message = list("Roll" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)

    def btnlm (self):
        radio.stopListening()
        a = self.left.intValue()
        a = a-1
        self.left.display(a)
        message = list("Roll" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)

    def btndp (self):
        radio.stopListening()
        a = self.down.intValue()
        a = a+1
        self.down.display(a)
        message = list("Yaw" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)

    def btndm(self):
        radio.stopListening()
        a = self.down.intValue()
        a = a - 1
        self.down.display(a)
        message = list("Yaw" + str(a) + "")
        while len(message) < 32:
            message.append(0)
        radio.write(message)

class ThreadClass(QtCore.QThread) :
    def __init__(self, parent= None):
        super(ThreadClass, self).__init__(parent)

    def run(self):

       while 1:


           message = list("Connection...")
           while len(message) < 32:
               message.append(0)

           radio.stopListening()
           radio.write(message)
           radio.startListening()
           self.sleep(0.5)

           if not radio.available(0):
               self.info.setText("Recherche de drone..")
               self.sleep(0.5)


           if radio.available(0):
               self.info.setText("Drone connecté")
               self.sleep(0.5)








a =QtGui.QApplication(sys.argv)

app = MainG()
app.show()

a.exec_()
