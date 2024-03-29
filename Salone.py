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
                stringaDalFile = a.read()
                jsonRecuperato = json.loads(stringaDalFile)

                for singoloAppuntamento in jsonRecuperato:
                    cliente = Cliente(singoloAppuntamento["cliente"]["nome"],singoloAppuntamento["cliente"]["cognome"], singoloAppuntamento["cliente"]["email"])
                    appuntamento = Appuntamento(singoloAppuntamento["data"], singoloAppuntamento["ora"], singoloAppuntamento["tipo_di_servizio"], cliente)
                    self.utente.append(appuntamento)
                pass
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
        c=0
        while c < len(self.utente) :
            if appuntamento.data == self.utente[c].data and appuntamento.ora == self.utente[c].ora:
                self.utente.pop(c)

            c=c+1
        self.saveUtente()
    
    def modificaUtente(self, vecchioAppuntamento, nuovoAppuntamento):
        if vecchioAppuntamento in self.utente:
            posizione=self.utente.index(vecchioAppuntamento)
            self.utente[posizione]=nuovoAppuntamento
        else:
            print("Questo appuntamento non esiste")
    
    def getJSON(self):
        risultato = []
        for appuntamento in self.utente:
            risultato.append(
                {
                    "cliente":{
                    "nome":appuntamento.cliente.nome,
                    "cognome":appuntamento.cliente.cognome,
                    "email":appuntamento.cliente.email
                    },
                    "data":appuntamento.data,
                    "ora":appuntamento.ora,
                    "tipo_di_servizio":appuntamento.tipo_di_servizio
                    })
        return risultato