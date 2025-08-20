def elenca(studenti):
    """
    Elenca le classi e i relativi studenti.

    Parametri:
    ---------
    studenti: lista delle classi

    Return:
    -------
    Print delle classi e dei relativi studenti

    """
    for lista in studenti:
        print(lista[0])
        for studente in lista[1]:
            print(f'\t {studente}')


def aggiungi(studenti):
    """
    Aggiunge uno studente alla classe corrispondente
    entrambe le variabili sono richieste allo user.

    Parametri:
    ---------
    studenti: lista degli studenti

    Return:
    -------
    Print della lista aggiornata degli studenti

    """

    classe = int(input("Inserisci la classe: "))
    studente = input("Inserisci il nome e cognome dello studente: ")
    aggiunta = False

    for lista in studenti:
        if lista[0] == classe:
            lista[1].append(studente)
            aggiunta = True
            print("Studente aggiunto con successo.")
            break
    if not aggiunta:
        studenti.append([classe, [studente]])
        print("Classe creata e studente aggiunto con successo.")

    print("Lista aggiornata degli studenti:")
    elenca(studenti)


def cerca(studenti):
    """
    Cerca uno studente nella lista e restituisce la sua classe.

    Parametri:
    ---------
    studenti: lista degli studenti

    Return:
    -------
    Print della classe dello studente cercato

    """
    nome_studente = input("Inserisci il nome e cognome dello studente da cercare: ")
    trovato = False

    for lista in studenti:
        if nome_studente in lista[1]:
            print(f"Lo studente {nome_studente} si trova nella classe {lista[0]}.")
            trovato = True
            break

    if not trovato:
        print(f"Lo studente {nome_studente} non è stato trovato.")