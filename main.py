from utils import funzioni
def main():
    dati_studenti = [[1, ["Pasquale Fidanza"]], [2, ["Flavia De Rinaldis"]]]
    print("menu:")
    print("1. Aggiungi studenti")
    print("2. Elenca Studenti")
    print("3. Cerca Studente")

    user_input = input("seleziona la tua scelta: ")

    if user_input == "1":
        studente = input("Inserisci la classe e il nome e cognome dello studente: ")
        # funzioni.aggiungi(dati_studenti, studente)
    elif user_input == "2":
        print("Ecco la lista delle classi e dei relativi studenti.")
        funzioni.elenca(dati_studenti)
    else:
        user_input = input("Inserisci nome e cognome dello studente che vuoi cercare: ")
        # funzioni.cerca(studente)

    # for lista in dati_studenti:
    #     print(lista)

if __name__ == "__main__":
    main()
    print("eseguito")