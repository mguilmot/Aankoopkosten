### Pas de volgende lijnen aan :-)
bedrag=200000
inleg=10000
beschrijf="groot"
intrest=0.0255
jaren=25
inlegextra=5000
aantalberekeningen=3

### Klik nu op run bovenaan

class berAfbet(object):
    def __init__(self,bedrag,intrest,jaren,inleg,beschrijf):
        self.bedrag=bedrag
        self.intrest=intrest
        self.jaren=jaren
        self.inleg=inleg
        self.beschrijf=beschrijf
    def berBeschrijf(self):
        '''
        Berekent de registratierechten.
        Verwacht een string "klein" of "groot"
        Resulteert in een float
        '''
        if self.beschrijf=="klein":
            return self.getBedrag()*0.05
        else:
            return self.getBedrag()*0.1
    def berNotaris(self):
        aktekosten=1100
        schijven={7500:0.0446,17500:0.0285,30000:0.0228,45495:0.0171,64095:0.0114,250095:0.0057,100000000:0.00057}
        bedNotaris=0.00
        vorigeSchijf=0
        for i in sorted(schijven):
            schijven_bedrag=i
            schijven_percent=schijven[i]
            tijdelijk=self.getBedrag()-schijven_bedrag
            if tijdelijk>0:
                verschil=schijven_bedrag-vorigeSchijf
            else:
                verschil=self.getBedrag()-vorigeSchijf
            if verschil<0:
                verschil=0
            #print(verschil,schijven_percent,verschil*schijven_percent)
            bedNotaris+=verschil*schijven_percent
            vorigeSchijf=schijven_bedrag
        return bedNotaris*1.21+aktekosten # (BTW = 21%)
    def berLening(self):
        lening=self.getBedrag()-self.getInleg()
        jaren=self.getJaren()
        intrest=self.getIntrest()/12
        periodes=jaren*12
        afbetaling=lening*(intrest*(1+intrest)**periodes)/((1+intrest)**periodes-1)
        return afbetaling
    def getBedrag(self):
        return self.bedrag
    def getIntrest(self):
        return self.intrest
    def getJaren(self):
        return self.jaren
    def getInleg(self):
        return self.inleg
    def __str__(self):
        #return str(self.getBedrag())+","+str(self.getIntrest())+","+str(self.getJaren())
        return self.printData()
    def printData(self):
        print("Berekening aankoopkosten aankoop huis.")
        print(mijnBer.getBedrag(),",",mijnBer.getInleg(),"inleg",end=", ")
        print(mijnBer.getJaren(),"jaar aan",str(mijnBer.getIntrest()*100)+"%",end=", ")
        print(beschrijf,"beschrijf")
        print("Beschrijf:",int(mijnBer.berBeschrijf()),", akte:",int(mijnBer.berNotaris()),", totaal",int(mijnBer.berBeschrijf()+mijnBer.berNotaris()))
        print("Afbetaling: ",int(mijnBer.berLening()),"per maand")
        return ""

for i in range(aantalberekeningen):
  mijnBer=berAfbet(bedrag,intrest,jaren,inleg,beschrijf)
  print(mijnBer)
  inleg+=inlegextra
