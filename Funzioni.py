from Salone import *


def main():
    while True:
        try:
            print("1) Aggiungere un appuntamento")
            print("2) Eliminare un appuntamento")
            print("3) Modifica un appuntamento")
            print("4) EXIT")
            scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")

            salone= Salone("Utenti.json")

            salone.caricaUtente()

            if scelta == '1':
                Nome=input("Inserisci il nome: ")
                Cognome=input("Inserisci il cognome: ")
                Email=input("Inserisci il email: ")
                Data=input("Inserisci il la data: ")
                Ora=input("Inserisci l'ora: ")
                Servizio=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(Nome,Cognome,Email)
                appuntamento=Appuntamento(Data,Ora,Servizio,cliente)

                salone.aggUtente(appuntamento)  
                salone.saveUtente()

            elif scelta == '2':
                Nome=input("Inserisci il nome: ")
                Cognome=input("Inserisci il cognome: ")
                Email=input("Inserisci il email: ")
                Data=input("Inserisci il la data: ")
                Ora=input("Inserisci l'ora: ")
                Servizio=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(Nome,Cognome,Email)
                appuntamento=Appuntamento(Data,Ora,Servizio,cliente)
                salone.delUtente(appuntamento)         
            elif scelta == '3':
                Nome=input("Inserisci il nome: ")
                Cognome=input("Inserisci il cognome: ")
                Email=input("Inserisci il email: ")
                Data=input("Inserisci il la data: ")
                Ora=input("Inserisci l'ora: ")
                Servizio=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(Nome,Cognome,Email)
                appuntamento=Appuntamento(Data,Ora,Servizio,cliente)
                salone.delUtente(appuntamento)  

                print("Adesso Re-inserisci i dati: ")

                Nome=input("Inserisci il nome: ")
                Cognome=input("Inserisci il cognome: ")
                Email=input("Inserisci il email: ")
                Data=input("Inserisci il la data: ")
                Ora=input("Inserisci l'ora: ")
                Servizio=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(Nome,Cognome,Email)
                appuntamento=Appuntamento(Data,Ora,Servizio,cliente)

                salone.aggUtente(appuntamento)  
                salone.saveUtente()

            elif scelta == '4':
                print("Uscita dal programma.")
                break

            else:
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print("Si è verificato un errore:", e)

if __name__ == "__main__":
    main()