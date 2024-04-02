from Salone import *  # Importa la classe Salone dal modulo Salone

def main():
    while True:  # Loop finché l'utente non sceglie di uscire
        try:  # Gestione delle eccezioni
            # Stampa il menu delle opzioni
            print("1) Aggiungere un appuntamento")
            print("2) Eliminare un appuntamento")
            print("3) Modifica un appuntamento")
            print("4) EXIT")
            # Richiede all'utente di inserire la scelta
            scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")

            # Crea un'istanza del Salone utilizzando il file "Utenti.json"
            salone = Salone("Utenti.json")

            # Carica gli utenti dal file JSON
            salone.caricaUtente()

            if scelta == '1':
                # Richiesta di input per aggiungere un nuovo appuntamento
                Nome = input("Inserisci il nome: ")
                Cognome = input("Inserisci il cognome: ")
                Email = input("Inserisci il email: ")
                Data = input("Inserisci il la data: ")
                Ora = input("Inserisci l'ora: ")
                Servizio = input("Inserisci il tipo di servizio: ")

                # Creazione di un'istanza di Cliente e Appuntamento
                cliente = Cliente(Nome, Cognome, Email)
                appuntamento = Appuntamento(Data, Ora, Servizio, cliente)

                # Aggiunta dell'appuntamento al Salone e salvataggio nel file JSON
                salone.aggUtente(appuntamento)
                salone.saveUtente()

            elif scelta == '2':
                # Richiesta di input per eliminare un appuntamento
                Nome = input("Inserisci il nome: ")
                Cognome = input("Inserisci il cognome: ")
                Email = input("Inserisci il email: ")
                Data = input("Inserisci il la data: ")
                Ora = input("Inserisci l'ora: ")
                Servizio = input("Inserisci il tipo di servizio: ")

                # Creazione di un'istanza di Cliente e Appuntamento
                cliente = Cliente(Nome, Cognome, Email)
                appuntamento = Appuntamento(Data, Ora, Servizio, cliente)

                # Eliminazione dell'appuntamento dal Salone
                salone.delUtente(appuntamento)

            elif scelta == '3':
                # Richiesta di input per modificare un appuntamento
                Nome = input("Inserisci il nome: ")
                Cognome = input("Inserisci il cognome: ")
                Email = input("Inserisci il email: ")
                Data = input("Inserisci il la data: ")
                Ora = input("Inserisci l'ora: ")
                Servizio = input("Inserisci il tipo di servizio: ")

                # Creazione di un'istanza di Cliente e Appuntamento per eliminare l'appuntamento esistente
                cliente = Cliente(Nome, Cognome, Email)
                appuntamento = Appuntamento(Data, Ora, Servizio, cliente)
                salone.delUtente(appuntamento)

                # Richiesta di reinserimento dei dati per creare un nuovo appuntamento
                print("Adesso Re-inserisci i dati: ")
                Nome = input("Inserisci il nome: ")
                Cognome = input("Inserisci il cognome: ")
                Email = input("Inserisci il email: ")
                Data = input("Inserisci il la data: ")
                Ora = input("Inserisci l'ora: ")
                Servizio = input("Inserisci il tipo di servizio: ")

                # Creazione di un nuovo appuntamento con i dati reinseriti
                cliente = Cliente(Nome, Cognome, Email)
                appuntamento = Appuntamento(Data, Ora, Servizio, cliente)

                # Aggiunta del nuovo appuntamento al Salone e salvataggio nel file JSON
                salone.aggUtente(appuntamento)
                salone.saveUtente()

            elif scelta == '4':
                # Uscita dal programma
                print("Uscita dal programma.")
                break

            else:
                # Messaggio di errore se l'utente inserisce un'opzione non valida
                print("Scelta non valida. Riprova.")

        except Exception as e:
            # Gestione delle eccezioni generiche
            print("Si è verificato un errore:", e)

if __name__ == "__main__":
    main()