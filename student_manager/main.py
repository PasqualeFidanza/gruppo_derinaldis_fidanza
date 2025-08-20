from utils import funzioni

def main():
    dati_studenti = [[1, ["Pasquale Fidanza"]], [2, ["Flavia De Rinaldis"]]]
    print("menu:")
    print("1. Aggiungi studenti")
    print("2. Elenca Studenti")
    print("3. Cerca Studente")

    user_input = input("seleziona la tua scelta: ")

    if user_input == "1":
        funzioni.aggiungi(dati_studenti)

    elif user_input == "2":
        print("Ecco la lista delle classi e dei relativi studenti.")
        funzioni.elenca(dati_studenti)

    else:
        funzioni.cerca(dati_studenti)


if __name__ == "__main__":
    main()
    print("eseguito")