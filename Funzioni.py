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


            if scelta == '1':
                a=input("Inserisci il nome: ")
                b=input("Inserisci il cognome: ")
                c=input("Inserisci il email: ")
                d=input("Inserisci il la data: ")
                e=input("Inserisci l'ora: ")
                f=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(a,b,c)
                appuntamento=Appuntamento(d,e,f,cliente)

                salone.aggUtente(appuntamento)  
                # cliente.aggAppuntamento(appuntamento)
                salone.saveUtente()

            elif scelta == '2':
                # Chiamata alla funzione per eliminare un appuntamento
                pass  # Aggiungi il codice qui

            elif scelta == '3':
                # Chiamata alla funzione per modificare un appuntamento
                pass  # Aggiungi il codice qui

            elif scelta == '4':
                print("Uscita dal programma.")
                break

            else:
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print("Si è verificato un errore:", e)

if __name__ == "__main__":
    main()