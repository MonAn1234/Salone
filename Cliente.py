class Cliente:
    def __init__(self, nome, cognome, email):
        # Inizializzazione della classe Cliente con nome, cognome, email e una lista di storico appuntamenti
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.storico_appuntamenti = []

    def aggAppuntamento(self, nuovoAppuntamento):
        # Aggiunge un nuovo appuntamento alla lista degli appuntamenti dello storico
        self.storico_appuntamenti.append(nuovoAppuntamento)