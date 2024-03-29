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
        with open(self.locazioneFile) as fileJson:
            json.dumps(self.utente, fileJson, indent=4)

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

    
