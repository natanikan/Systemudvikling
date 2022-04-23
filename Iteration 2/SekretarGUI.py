import time
from Database import Database
from PyQt6 import QtWidgets, uic
db = Database()

class SekretarGUI(QtWidgets.QWidget):
    def __init__(self):
        super(SekretarGUI, self).__init__()
        uic.loadUi('UI/Sekretar.ui', self)
        self.show()
        x = ["1","2","3"]
        req = db.showAnmodninger()
        for i in req:
            self.listRequest.addItem(f"{i[0]}, "+i[1]+", "+i[2]+", "+i[3]+", "+i[4])
        self.listRequest.itemSelectionChanged.connect(self.valgt_foresporgsel)
        self.afvisBooking.clicked.connect(self.afvis)
        self.godkendBooking.clicked.connect(self.godkend)


    def valgt_foresporgsel(self):
        valg = [item.text() for item in self.listRequest.selectedItems()]
        primarykey_anmodninger = valg[0][:2]
        return primarykey_anmodninger.strip(',')

    def afvis(self):
        db.delAnmodning(self.valgt_foresporgsel())  # Sletter anmodning i database
        listItems = self.listRequest.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listRequest.takeItem(self.listRequest.row(item))

    def godkend(self):
        underviser = ''.join(db.getUnderviser(self.valgt_foresporgsel()))
        kursus = ''.join(db.getKursus(self.valgt_foresporgsel()))
        dato = ''.join(db.getDato(self.valgt_foresporgsel()))
        tid = ''.join(db.getTid(self.valgt_foresporgsel()))
        lokale = self.lokaleDropdown.currentText()
        db.addSkema(underviser, kursus, lokale, dato, tid)
        db.delAnmodning(self.valgt_foresporgsel())
        listItems = self.listRequest.selectedItems()
        if not listItems: return
        for item in listItems:
            self.listRequest.takeItem(self.listRequest.row(item))













