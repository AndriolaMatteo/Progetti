def menu():
    print("\nMenu Rubrica Telefonica")
    print("1) Inserimento del numero di telefono")
    print("2) Modifica numero di telefono")
    print("3) Stampa rubrica ordinata (per nominativo o città)")
    print("4) Eliminazione numero di telefono")
    print("5) Scrittura su file 'Rubrica.txt'")
    print("6) Lettura dal file 'Rubrica.txt'")
    print("0) Uscita dal programma")

def inserisci_contatto(rubrica):
    nominativo = input("Inserisci il nominativo: ")
    telefono1 = input("Inserisci il telefono1: ")
    telefono2 = input("Inserisci il telefono2 (opzionale): ")
    indirizzo = input("Inserisci l'indirizzo: ")
    citta = input("Inserisci la città: ")
    societa = input("Inserisci la società: ")
    
    contatto = {
        'nominativo': nominativo,
        'telefono1': telefono1,
        'telefono2': telefono2,
        'indirizzo': indirizzo,
        'citta': citta,
        'societa': societa
    }


    for i in range(len(rubrica)):
        if rubrica[i] is None:
            rubrica[i] = contatto
            return
    rubrica += [contatto]

def modifica_contatto(rubrica):
    nominativo = input("Inserisci il nominativo del contatto da modificare: ")
    for contatto in rubrica:
        if contatto and contatto['nominativo'] == nominativo:
            telefono1 = input(f"Modifica telefono1 ({contatto['telefono1']}): ")
            telefono2 = input(f"Modifica telefono2 ({contatto['telefono2']}): ")
            indirizzo = input(f"Modifica indirizzo ({contatto['indirizzo']}): ")
            citta = input(f"Modifica città ({contatto['citta']}): ")
            societa = input(f"Modifica società ({contatto['societa']}): ")
            contatto.update({
                'telefono1': telefono1,
                'telefono2': telefono2,
                'indirizzo': indirizzo,
                'citta': citta,
                'societa': societa
            })
            return
    print("Contatto non trovato!")

def stampa_rubrica(rubrica):
    criterio = input("Ordinare per 'nominativo' o 'citta'? ")
    rubrica_filtrata = [contatto for contatto in rubrica if contatto is not None]
    
    if criterio == 'nominativo':
        rubrica_ordinata = sorted(rubrica_filtrata, key=lambda x: x['nominativo'])
    elif criterio == 'citta':
        rubrica_ordinata = sorted(rubrica_filtrata, key=lambda x: x['citta'])
    else:
        print("Criterio non valido!")
        return

    for contatto in rubrica_ordinata:
        print(f"Nominativo: {contatto['nominativo']}, Telefono1: {contatto['telefono1']}, Telefono2: {contatto['telefono2']}, Indirizzo: {contatto['indirizzo']}, Città: {contatto['citta']}, Società: {contatto['societa']}")

def elimina_contatto(rubrica):
    nominativo = input("Inserisci il nominativo del contatto da eliminare: ")
    for i in range(len(rubrica)):
        if rubrica[i] and rubrica[i]['nominativo'] == nominativo:
            rubrica[i] = None
            print("Contatto eliminato!")
            return
    print("Contatto non trovato!")

def scrittura_su_file(rubrica):
    with open('Rubrica.txt', 'w') as file:
        for contatto in rubrica:
            if contatto is not None:
                file.write(f"{contatto['nominativo']};{contatto['telefono1']};{contatto['telefono2']};{contatto['indirizzo']};{contatto['citta']};{contatto['societa']}\n")
    print("Rubrica salvata su 'Rubrica.txt'!")

def lettura_da_file():
    rubrica = []
    try:
        with open('Rubrica.txt', 'r') as file:
            for line in file:
                nominativo, telefono1, telefono2, indirizzo, citta, societa = line.strip().split(';')
                contatto = {
                    'nominativo': nominativo,
                    'telefono1': telefono1,
                    'telefono2': telefono2,
                    'indirizzo': indirizzo,
                    'citta': citta,
                    'societa': societa
                }
                rubrica += [contatto]
        print("Rubrica caricata da 'Rubrica.txt'!")
    except FileNotFoundError:
        print("File non trovato!")
    return rubrica

def main():
    rubrica = []
    while True:
        menu()
        scelta = input("Scegli un'opzione: ")
        if scelta == '1':
            inserisci_contatto(rubrica)
        elif scelta == '2':
            modifica_contatto(rubrica)
        elif scelta == '3':
            stampa_rubrica(rubrica)
        elif scelta == '4':
            elimina_contatto(rubrica)
        elif scelta == '5':
            scrittura_su_file(rubrica)
        elif scelta == '6':
            rubrica = lettura_da_file()
        elif scelta == '0':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida! Riprova.")

if __name__ == "__main__":
    main()
