'''
    Berekent aankoopkosten met grafische vormgeving.
    Hangt af van PyQT5
'''

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from graphGUI import Ui_Aankoopkosten

''' To make the icon work in the taskbar in Win7+, ctype is needed'''
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class runApplication(Ui_Aankoopkosten):
    def __init__(self):
        self.app=QApplication(sys.argv)
        self.window=QWidget()
        self.ui=Ui_Aankoopkosten()
        self.setdefaults()
        self.run()
        
    def setdefaults(self):
        self.ui.aktekosten=0
        self.ui.registratiekosten=0
        self.ui.totaal=0
        self.ui.afbetaling=0
    
    def run(self):
        self.ui.setupUi(self.window)
        self.buttonactions()
        self.window.show()
        self.Quit()
    
    def Quit(self):
        sys.exit(self.app.exec_())
    
    def calculate(self):
        self.ui.aktekosten=1100
        self.bereken_notaris()
        self.bereken_registratiekosten()
        self.bereken_lening()
        self.update()
    
    def update(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.totaal=self.ui.aktekosten+self.ui.registratiekosten
        self.ui.textResultaat.setHtml(_translate("Aankoopkosten", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Berekening aankoopkosten en afbetaling</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><b>Aktekosten</b>: " + str(self.ui.aktekosten) + "</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><b>Registratie</b>: " + str(self.ui.registratiekosten) + "</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><b>Totaal beschrijf</b>: " + str(self.ui.totaal) + "</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><b>Afbetaling per maand</b>: " + str(self.ui.afbetaling) +"</p></body></html>"))
    
    def bereken_notaris(self):
        self.bedrag_aankoopprijs=int(self.ui.Aankoopprijs.text().replace('.',''))
        self.schijven={7500:0.0446,17500:0.0285,30000:0.0228,45495:0.0171,64095:0.0114,250095:0.0057,100000000:0.00057}
        bedNotaris=0.00
        vorigeSchijf=0
        for i in sorted(self.schijven):
            schijven_bedrag=i
            schijven_percent=self.schijven[i]
            tijdelijk=self.bedrag_aankoopprijs-schijven_bedrag
            if tijdelijk>0:
                verschil=schijven_bedrag-vorigeSchijf
            else:
                verschil=self.bedrag_aankoopprijs-vorigeSchijf
            if verschil<0:
                verschil=0
            bedNotaris+=verschil*schijven_percent
            vorigeSchijf=schijven_bedrag
        self.ui.aktekosten+= int(bedNotaris*1.21)
    
    def bereken_registratiekosten(self):
        self.bedrag_aankoopprijs=int(self.ui.Aankoopprijs.text().replace('.',''))
        if self.ui.Beschrijf.currentText()=="klein":
            self.ui.registratiekosten = int(self.bedrag_aankoopprijs*0.05)
        else:
            self.ui.registratiekosten = int(self.bedrag_aankoopprijs*0.1)

    def bereken_lening(self):
        self.bedrag_aankoopprijs=int(self.ui.Aankoopprijs.text().replace('.',''))
        self.bedrag_inleg=int(self.ui.Inleg.text().replace('.',''))
        self.jaren_afbetaling=int(self.ui.Jaren.text())
        self.intrest=float(self.ui.Percent.text())
        lening=self.bedrag_aankoopprijs-self.bedrag_inleg
        jaren=self.jaren_afbetaling
        intrest=self.intrest/12
        periodes=jaren*12
        self.ui.afbetaling=int(lening*(intrest*(1+intrest)**periodes)/((1+intrest)**periodes-1))

    def buttonactions(self):
        self.ui.pushButtonAfsluiten.clicked.connect(self.Quit)
        self.ui.pushButtonBereken.clicked.connect(self.calculate)

if __name__ == '__main__':
    runApplication()

