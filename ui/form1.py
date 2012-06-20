# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created: Tue Jun 19 16:59:42 2012
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
import handmade_socket
import sys 

class Form1(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form1")


        Form1Layout = QHBoxLayout(self,11,6,"Form1Layout")
        Form1Layout.setResizeMode(QLayout.FreeResize)

        layout15 = QVBoxLayout(None,0,6,"layout15")

        self.data_field = QLabel(self,"data_field")
        self.data_field.setMinimumSize(QSize(280,40))

        layout15.addWidget(self.data_field)
        spacer7 = QSpacerItem(20,35,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout15.addItem(spacer7)

        layout14 = QHBoxLayout(None,0,6,"layout14")

        self.text_field = QLineEdit(self,"text_field")
        layout14.addWidget(self.text_field)
        spacer6 = QSpacerItem(50,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout14.addItem(spacer6)

        self.pushButton1 = QPushButton(self,"pushButton1")
        layout14.addWidget(self.pushButton1)
        layout15.addLayout(layout14)
        spacer8 = QSpacerItem(20,90,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout15.addItem(spacer8)

        layout10 = QHBoxLayout(None,0,6,"layout10")
        spacer11 = QSpacerItem(90,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout10.addItem(spacer11)

        self.pushButton2 = QPushButton(self,"pushButton2")
        layout10.addWidget(self.pushButton2)
        spacer12 = QSpacerItem(100,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout10.addItem(spacer12)
        layout15.addLayout(layout10)
        Form1Layout.addLayout(layout15)

        self.languageChange()

        self.resize(QSize(332,271).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton1,SIGNAL("clicked()"),self.pushButton1_clicked)
        self.connect(self.pushButton2,SIGNAL("clicked()"),self.pushButton2_clicked)

        self.socket = handmade_socket.handmade_socket()
        self.socket.sock_connect("localhost", 4444)

    def languageChange(self):
        self.setCaption(self.__tr("QT GUI"))
        self.data_field.setText(QString.null)
        self.pushButton1.setText(self.__tr("Send to server"))
        self.pushButton2.setText(self.__tr("Exit"))


    def pushButton1_clicked(self):
        if len(self.text_field.text()) == 0:
             return
        self.socket.sock_send(self.text_field.text())
        msg = self.socket.sock_receive()
        msg = msg.decode("utf-16")
        self.data_field.setText( msg )
        self.data_field.repaint()

    def pushButton2_clicked(self):
        self.socket.sock_send("exit")
        self.socket.sock_close()
        exit()       

    def __tr(self,s,c = None):
        return qApp.translate("Form1",s,c)
