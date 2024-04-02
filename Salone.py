from Cliente import *  # Importa la classe Cliente dal modulo Cliente
from Appuntamento import *  # Importa la classe Appuntamento dal modulo Appuntamento
import json  # Importa il modulo json per la gestione dei file JSON

class Salone:
    def __init__(self, locazioneFile):
        # Inizializza la classe Salone con la locazione del file JSON e una lista di utenti (appuntamenti)
        self.locazioneFile = locazioneFile
        self.utente = []

    def caricaUtente(self):
        try:
            # Tenta di aprire il file JSON in modalità lettura
            with open(self.locazioneFile, "r+") as a:
                # Legge il contenuto del file e lo converte in formato JSON
                stringaDalFile = a.read()
                jsonRecuperato = json.loads(stringaDalFile)

                # Itera su ogni appuntamento recuperato dal file
                for singoloAppuntamento in jsonRecuperato:
                    # Crea un'istanza di Cliente e Appuntamento utilizzando i dati recuperati dal file
                    cliente = Cliente(singoloAppuntamento["cliente"]["nome"],
                                      singoloAppuntamento["cliente"]["cognome"],
                                      singoloAppuntamento["cliente"]["email"])
                    appuntamento = Appuntamento(singoloAppuntamento["data"],
                                                singoloAppuntamento["ora"],
                                                singoloAppuntamento["tipo_di_servizio"],
                                                cliente)
                    # Aggiunge l'appuntamento alla lista degli utenti
                    self.utente.append(appuntamento)
        except FileNotFoundError:
            print("FILE NON TROVATO")

    def saveUtente(self):
        # Ottiene il contenuto JSON della lista degli utenti
        stringaDaScrivere = self.getJSON()
        if len(stringaDaScrivere) > 0:
            # Scrive il contenuto JSON nel file
            with open(self.locazioneFile, "w+") as fileDaScrivere:
                fileDaScrivere.write(json.dumps(stringaDaScrivere, indent=4))

    def aggUtente(self, appuntamento):
        # Aggiunge un nuovo appuntamento alla lista degli utenti
        self.utente.append(appuntamento)

    def delUtente(self, appuntamento):
        # Elimina un appuntamento dalla lista degli utenti
        c = 0
        while c < len(self.utente):
            if appuntamento.data == self.utente[c].data and appuntamento.ora == self.utente[c].ora:
                self.utente.pop(c)
            c += 1
        # Salva le modifiche nel file JSON
        self.saveUtente()
    
    def modificaUtente(self, vecchioAppuntamento, nuovoAppuntamento):
        # Modifica un appuntamento nella lista degli utenti
        if vecchioAppuntamento in self.utente:
            posizione = self.utente.index(vecchioAppuntamento)
            self.utente[posizione] = nuovoAppuntamento
        else:
            print("Questo appuntamento non esiste")
    
    def getJSON(self):
        # Ottiene il contenuto JSON della lista degli utenti
        risultato = []
        for appuntamento in self.utente:
            # Crea un dizionario per rappresentare l'appuntamento in formato JSON
            risultato.append(
                {
                    "cliente": {
                        "nome": appuntamento.cliente.nome,
                        "cognome": appuntamento.cliente.cognome,
                        "email": appuntamento.cliente.email
                    },
                    "data": appuntamento.data,
                    "ora": appuntamento.ora,
                    "tipo_di_servizio": appuntamento.tipo_di_servizio
                }
            )
        return risultato