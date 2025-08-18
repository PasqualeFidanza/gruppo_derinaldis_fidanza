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


def aggiungi(lista):
    pass


def cerca():
    pass