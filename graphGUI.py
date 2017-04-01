# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Aankoopkosten(object):
    def setupUi(self, Aankoopkosten):
        Aankoopkosten.setObjectName("Aankoopkosten")
        Aankoopkosten.resize(489, 247)
        Aankoopkosten.setMinimumSize(QtCore.QSize(489, 247))
        Aankoopkosten.setMaximumSize(QtCore.QSize(489, 247))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Aankoopkosten.setWindowIcon(icon)
        self.Aankoopprijs = QtWidgets.QLineEdit(Aankoopkosten)
        self.Aankoopprijs.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.Aankoopprijs.setInputMask("")
        self.Aankoopprijs.setObjectName("Aankoopprijs")
        self.Percent = QtWidgets.QLineEdit(Aankoopkosten)
        self.Percent.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.Percent.setInputMask("")
        self.Percent.setObjectName("Percent")
        self.lblAankoopkosten = QtWidgets.QLabel(Aankoopkosten)
        self.lblAankoopkosten.setGeometry(QtCore.QRect(14, 30, 71, 20))
        self.lblAankoopkosten.setObjectName("lblAankoopkosten")
        self.lblPercent = QtWidgets.QLabel(Aankoopkosten)
        self.lblPercent.setGeometry(QtCore.QRect(38, 64, 47, 13))
        self.lblPercent.setObjectName("lblPercent")
        self.lblBeschrijf = QtWidgets.QLabel(Aankoopkosten)
        self.lblBeschrijf.setGeometry(QtCore.QRect(34, 154, 47, 13))
        self.lblBeschrijf.setObjectName("lblBeschrijf")
        self.Inleg = QtWidgets.QLineEdit(Aankoopkosten)
        self.Inleg.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.Inleg.setInputMask("")
        self.Inleg.setObjectName("Inleg")
        self.lblInleg = QtWidgets.QLabel(Aankoopkosten)
        self.lblInleg.setGeometry(QtCore.QRect(24, 89, 51, 20))
        self.lblInleg.setObjectName("lblInleg")
        self.textResultaat = QtWidgets.QTextEdit(Aankoopkosten)
        self.textResultaat.setGeometry(QtCore.QRect(250, 30, 221, 121))
        self.textResultaat.setObjectName("textResultaat")
        self.pushButtonBereken = QtWidgets.QPushButton(Aankoopkosten)
        self.pushButtonBereken.setGeometry(QtCore.QRect(50, 200, 75, 23))
        self.pushButtonBereken.setObjectName("pushButtonBereken")
        self.pushButtonAfsluiten = QtWidgets.QPushButton(Aankoopkosten)
        self.pushButtonAfsluiten.setGeometry(QtCore.QRect(130, 200, 75, 23))
        self.pushButtonAfsluiten.setObjectName("pushButtonAfsluiten")
        self.Jaren = QtWidgets.QLineEdit(Aankoopkosten)
        self.Jaren.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.Jaren.setObjectName("Jaren")
        self.lblJaren = QtWidgets.QLabel(Aankoopkosten)
        self.lblJaren.setGeometry(QtCore.QRect(48, 122, 31, 16))
        self.lblJaren.setObjectName("lblJaren")
        self.Beschrijf = QtWidgets.QComboBox(Aankoopkosten)
        self.Beschrijf.setGeometry(QtCore.QRect(90, 150, 69, 22))
        self.Beschrijf.setObjectName("Beschrijf")
        self.Beschrijf.addItem("")
        self.Beschrijf.addItem("")

        self.retranslateUi(Aankoopkosten)
        QtCore.QMetaObject.connectSlotsByName(Aankoopkosten)

    def retranslateUi(self, Aankoopkosten):
        _translate = QtCore.QCoreApplication.translate
        Aankoopkosten.setWindowTitle(_translate("Aankoopkosten", "Aankoopkosten"))
        self.Aankoopprijs.setText(_translate("Aankoopkosten", "220.000"))
        self.Aankoopprijs.setPlaceholderText(_translate("Aankoopkosten", "aankoopprijs"))
        self.Percent.setText(_translate("Aankoopkosten", "0.0255"))
        self.Percent.setPlaceholderText(_translate("Aankoopkosten", "percentage"))
        self.lblAankoopkosten.setText(_translate("Aankoopkosten", "Aankoopprijs"))
        self.lblPercent.setText(_translate("Aankoopkosten", "Percent"))
        self.lblBeschrijf.setText(_translate("Aankoopkosten", "Beschrijf"))
        self.Inleg.setText(_translate("Aankoopkosten", "10.000"))
        self.Inleg.setPlaceholderText(_translate("Aankoopkosten", "aankoopprijs"))
        self.lblInleg.setText(_translate("Aankoopkosten", "Extra inleg"))
        self.textResultaat.setHtml(_translate("Aankoopkosten", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.pushButtonBereken.setText(_translate("Aankoopkosten", "Bereken!"))
        self.pushButtonAfsluiten.setText(_translate("Aankoopkosten", "Afsluiten"))
        self.Jaren.setText(_translate("Aankoopkosten", "25"))
        self.lblJaren.setText(_translate("Aankoopkosten", "Jaren"))
        self.Beschrijf.setCurrentText(_translate("Aankoopkosten", "klein"))
        self.Beschrijf.setItemText(0, _translate("Aankoopkosten", "klein"))
        self.Beschrijf.setItemText(1, _translate("Aankoopkosten", "groot"))

