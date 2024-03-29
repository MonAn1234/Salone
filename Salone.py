from Cliente import *
from Appuntamento import *
import json

class Salone:
    def __init__(self, locazioneFile):
        self.locazioneFile=locazioneFile
        self.utente=[]

    def caricaUtente(self):
        try:
            with open(self.locazioneFile, "r+") as a:
                return json.loads(a)
        except FileNotFoundError:
            print("FILE NON TROVATO")

    def saveUtente(self):
        stringaDaScrivere = self.getJSON()
        if(len(stringaDaScrivere)>0):
            with open(self.locazioneFile, "w+") as fileDaScrivere:
                fileDaScrivere.write(json.dumps(stringaDaScrivere, indent=4))

    def aggUtente(self, appuntamento):
        self.utente.append(appuntamento)

    def delUtente(self,appuntamento):
        if appuntamento in self.utente:
            self.utente.remove(appuntamento)
        else:
            print("Appuntamento non esiste")
    
    def modificaUtente(self, vecchioAppuntamento, nuovoAppuntamento):
        if vecchioAppuntamento in self.utente:
            posizione=self.utente.index(vecchioAppuntamento)
            self.utente[posizione]=nuovoAppuntamento
        else:
            print("Questo appuntamento non esiste")
    
    def getJSON(self):
        risultato = []
        for appuntamento in self.utente:
            risultato.append({"nome":appuntamento.cliente.nome,"cognome":appuntamento.cliente.cognome,"email":appuntamento.cliente.email,"data":appuntamento.data,"ora":appuntamento.ora,"servizio":appuntamento.tipo_di_servizio})
        return risultato