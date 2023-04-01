# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 487)
        MainWindow.setSizeIncrement(QtCore.QSize(1, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Desktop/GitHub/Betsy/pngwing.com (5).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 30, 261, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.chatlog = QtWidgets.QTextEdit(self.frame)
        self.chatlog.setGeometry(QtCore.QRect(10, 10, 241, 291))
        self.chatlog.setObjectName("chatlog")
        self.userentry = QtWidgets.QTextEdit(self.frame)
        self.userentry.setGeometry(QtCore.QRect(10, 340, 171, 51))
        self.userentry.setObjectName("userentry")
        self.sendButton = QtWidgets.QPushButton(self.frame)
        self.sendButton.setGeometry(QtCore.QRect(190, 340, 61, 51))
        self.sendButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Desktop/GitHub/Betsy/pngwing.com (9).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendButton.setIcon(icon1)
        self.sendButton.setIconSize(QtCore.QSize(50, 50))
        self.sendButton.setFlat(True)
        self.sendButton.setObjectName("sendButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 10, 251, 191))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777210))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.applyButton = QtWidgets.QPushButton(self.groupBox_2)
        self.applyButton.setGeometry(QtCore.QRect(190, 150, 41, 31))
        self.applyButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Desktop/GitHub/Betsy/button_blank_red_14987.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("../../../Desktop/GitHub/Betsy/button_blank_green_14986.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.applyButton.setIcon(icon2)
        self.applyButton.setIconSize(QtCore.QSize(30, 29))
        self.applyButton.setFlat(True)
        self.applyButton.setObjectName("applyButton")
        self.systementry = QtWidgets.QTextEdit(self.groupBox_2)
        self.systementry.setGeometry(QtCore.QRect(10, 30, 221, 111))
        self.systementry.setObjectName("systementry")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(13, 150, 131, 26))
        self.comboBox.setObjectName("comboBox")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(340, 290, 261, 141))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../../../Desktop/GitHub/Betsy/pngwing.com (6).png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.currentprompttokens = QtWidgets.QLCDNumber(self.centralwidget)
        self.currentprompttokens.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.currentprompttokens.setObjectName("currentprompttokens")
        self.tokendisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.tokendisplay.setGeometry(QtCore.QRect(403, 220, 51, 21))
        self.tokendisplay.setObjectName("tokendisplay")
        self.tempdisplay = QtWidgets.QLCDNumber(self.centralwidget)
        self.tempdisplay.setGeometry(QtCore.QRect(553, 220, 51, 20))
        self.tempdisplay.setObjectName("tempdisplay")
        self.tokenSlider = QtWidgets.QSlider(self.centralwidget)
        self.tokenSlider.setGeometry(QtCore.QRect(390, 250, 71, 31))
        self.tokenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tokenSlider.setObjectName("tokenSlider")
        self.tempSlider = QtWidgets.QSlider(self.centralwidget)
        self.tempSlider.setGeometry(QtCore.QRect(550, 250, 71, 31))
        self.tempSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tempSlider.setObjectName("tempSlider")
        self.tokenlabel = QtWidgets.QLabel(self.centralwidget)
        self.tokenlabel.setGeometry(QtCore.QRect(320, 260, 60, 16))
        self.tokenlabel.setObjectName("tokenlabel")
        self.templabel = QtWidgets.QLabel(self.centralwidget)
        self.templabel.setGeometry(QtCore.QRect(480, 260, 60, 16))
        self.templabel.setObjectName("templabel")
        self.logo.raise_()
        self.frame.raise_()
        self.groupBox_2.raise_()
        self.currentprompttokens.raise_()
        self.tokendisplay.raise_()
        self.tempdisplay.raise_()
        self.tokenSlider.raise_()
        self.tempSlider.raise_()
        self.tokenlabel.raise_()
        self.templabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 22))
        self.menubar.setObjectName("menubar")
        self.menuAssistant = QtWidgets.QMenu(self.menubar)
        self.menuAssistant.setObjectName("menuAssistant")
        self.menuContextes = QtWidgets.QMenu(self.menubar)
        self.menuContextes.setObjectName("menuContextes")
        self.menuParam_tres = QtWidgets.QMenu(self.menubar)
        self.menuParam_tres.setObjectName("menuParam_tres")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionSoutenir_le_projet = QtWidgets.QAction(MainWindow)
        self.actionSoutenir_le_projet.setObjectName("actionSoutenir_le_projet")
        self.actionNouveau_Contexte = QtWidgets.QAction(MainWindow)
        self.actionNouveau_Contexte.setObjectName("actionNouveau_Contexte")
        self.actionSuprimmer_un_contexte = QtWidgets.QAction(MainWindow)
        self.actionSuprimmer_un_contexte.setObjectName("actionSuprimmer_un_contexte")
        self.actionNouvelle_seance_de_travail = QtWidgets.QAction(MainWindow)
        self.actionNouvelle_seance_de_travail.setObjectName("actionNouvelle_seance_de_travail")
        self.actionEnregistrer_la_seance_de_travail = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_la_seance_de_travail.setObjectName("actionEnregistrer_la_seance_de_travail")
        self.actionExporter_la_s_ance_de_travail = QtWidgets.QAction(MainWindow)
        self.actionExporter_la_s_ance_de_travail.setObjectName("actionExporter_la_s_ance_de_travail")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuAssistant.addAction(self.actionNouvelle_seance_de_travail)
        self.menuAssistant.addAction(self.actionEnregistrer_la_seance_de_travail)
        self.menuAssistant.addAction(self.actionExporter_la_s_ance_de_travail)
        self.menuAssistant.addSeparator()
        self.menuAssistant.addAction(self.actionQuitter)
        self.menuContextes.addAction(self.actionNouveau_Contexte)
        self.menuContextes.addAction(self.actionSuprimmer_un_contexte)
        self.menuAide.addAction(self.actionDocumentation)
        self.menuAide.addAction(self.actionSoutenir_le_projet)
        self.menubar.addAction(self.menuAssistant.menuAction())
        self.menubar.addAction(self.menuContextes.menuAction())
        self.menubar.addAction(self.menuParam_tres.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BETSY"))
        self.groupBox_2.setTitle(_translate("MainWindow", "SYSTEM"))
        self.tokenlabel.setText(_translate("MainWindow", "Tokens"))
        self.templabel.setText(_translate("MainWindow", "Temp"))
        self.menuAssistant.setTitle(_translate("MainWindow", "Assistant"))
        self.menuContextes.setTitle(_translate("MainWindow", "Contextes"))
        self.menuParam_tres.setTitle(_translate("MainWindow", "Paramétres"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionSoutenir_le_projet.setText(_translate("MainWindow", "Soutenir le projet"))
        self.actionNouveau_Contexte.setText(_translate("MainWindow", "Nouveau Contexte"))
        self.actionSuprimmer_un_contexte.setText(_translate("MainWindow", "Suprimmer un contexte"))
        self.actionNouvelle_seance_de_travail.setText(_translate("MainWindow", "Nouvelle seance de travail"))
        self.actionEnregistrer_la_seance_de_travail.setText(_translate("MainWindow", "Enregistrer la seance de travail "))
        self.actionExporter_la_s_ance_de_travail.setText(_translate("MainWindow", "Exporter la séance de travail"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())