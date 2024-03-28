class Cliente:
    def __init__(self,nome,cognome,email):
        self.nome=nome
        self.cognome=cognome
        self.email=email
        self.storico_appuntamenti=[]

    def aggAppuntamento(self,nuovoAppuntamenti):
        self.storico_appuntamenti.append(nuovoAppuntamenti) 