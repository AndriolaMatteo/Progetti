def inserisci_squadra():
    nome = input("inserisci il nome della squadra: ")
    colore_maglia = input("inserisci il colore della maglia: ")
    punteggio = int(input("inserisci il punteggio della squadra: "))
    nome_allenatore = input("inserisci il nome dell'allenatore: ")
    cognome_allenatore = input("inserisci il cognome dell'allenatore: ")
    titoli_vinti = int(input("inserisci il numero di titoli vinti dall'allenatore: "))
    allenatore = {"nome": nome_allenatore, "cognome": cognome_allenatore, "titoli_vinti": titoli_vinti}
    squadra = {"nome": nome, "colore_maglia": colore_maglia, "punteggio": punteggio, "allenatore": allenatore}
    return squadra


def ordina_per_punteggio(squadre):
    return sorted(squadre, key = lambda x: x["punteggio"], reverse=True)


def stampa_classifica(squadre):
    squadre_ordinate = ordina_per_punteggio(squadre)
    posizionamento = 1
    for squadra in squadre_ordinate:
        print(f"{posizionamento}. {squadra['nome']} - Punteggio: {squadra['punteggio']}")
        posizionamento += 1


def modifica_punteggio(squadre):
    nome_squadra = input("inserisci il nome della squadra a cui vuoi modificare il punteggio ottenuto: ")
    for squadra in squadre:
        if squadra["nome"] == nome_squadra:
            nuovo_punteggio = int(input("inserisci il nuovo punteggio: "))
            squadra["punteggio"] = nuovo_punteggio
            print("punteggio aggiornato")
            return
    print("squadra inesistente o non trovata")


def ordina_per_titoli(allenatori):
    for i in range(len(allenatori)):
        for k in range(i + 1, len(allenatori)):
            if allenatori[i]["titoli_vinti"] < allenatori[k]["titoli_vinti"]:
                allenatori[i], allenatori[k] = allenatori[k], allenatori[i]
    return allenatori


def stampa_classifica_titoli(squadre):
    allenatori = []
    for squadra in squadre:
        allenatori.append(squadra["allenatore"])
    allenatori_ordinati = ordina_per_titoli(allenatori)
    posizionamento = 1
    for allenatore in allenatori_ordinati:
        print(f"{posizionamento}. {allenatore['nome']} {allenatore['cognome']} - Titoli vinti: {allenatore['titoli_vinti']}")
        posizionamento += 1


def allenatori_titoli_vinti(squadre):
    titoli_input = int(input("inserisci il numero di titoli vinti: "))
    allenatori_con_titoli = 0
    for squadra in squadre:
        if squadra["allenatore"]["titoli_vinti"] == titoli_input:
            allenatori_con_titoli += 1
    print(f"il numero di allenatori che hanno vinto {titoli_input} titoli è {allenatori_con_titoli}.")


def stampa_squadre_con_punteggio(squadre):
    punteggio_input = int(input("inserisci il punteggio minimo ottenuto dalle squadre: "))
    squadre_con_punteggio = []
    for squadra in squadre:
        if squadra["punteggio"] > punteggio_input:
            squadre_con_punteggio.append(squadra)
    if squadre_con_punteggio:
        for squadra in squadre_con_punteggio:
            print(f"{squadra['nome']} - punteggio: {squadra['punteggio']}")
    else:
        print("non sono state trovate squadre con un punteggio maggiore di quello inserito precedentemente")


def squadre_con_allenatori_con_titoli_vinti(squadre):
    titoli_input = int(input("inserisci il numero di titoli vinti: "))
    squadre_con_allenatori_titoli = []
    for squadra in squadre:
        if squadra["allenatore"]["titoli_vinti"] > titoli_input:
            squadre_con_allenatori_titoli.append(squadra)
    if squadre_con_allenatori_titoli:
        for squadra in squadre_con_allenatori_titoli:
            allenatore = squadra["allenatore"]
            print(f"{squadra['nome']} - Allenatore: {allenatore['nome']} {allenatore['cognome']} - Titoli vinti: {allenatore['titoli_vinti']}")
    else:
        print("non sono state trovate squadre il cui allenatore ha un numero di titoli maggiore di quello inserito precentemente")


def main():
    squadre = []

    while True:
        print("\nMenu:")
        print("1) inserimento dati delle squadre")
        print("2) stampare la classifica delle squadre in ordine decrescente di punteggio")
        print("3) modificare i punti di una squadra con input da tastiera")
        print("4) stampare classifica titoli degli allenatori in ordine decrescente di titoli")
        print("5) numero totale di allenatori che hanno vinto Y titoli, con Y preso in input")
        print("6) stampa squadre con più di Y punti in classifica (Y preso in input)")
        print("7) stampare squadre con allenatori che hanno vinto più di Y titoli (Y preso in input)")
        print("0) esci")

        scelta = input("scelta: ")

        if scelta == '1':
            squadra = inserisci_squadra()
            squadre.append(squadra)
        elif scelta == '2':
            stampa_classifica(squadre)
        elif scelta == '3':
            modifica_punteggio(squadre)
        elif scelta == '4':
            stampa_classifica_titoli(squadre)
        elif scelta == '5':
            allenatori_titoli_vinti(squadre)
        elif scelta == '6':
            stampa_squadre_con_punteggio(squadre)
        elif scelta == '7':
            squadre_con_allenatori_con_titoli_vinti(squadre)
        elif scelta == '0':
            break
        else:
            print("scelta non valida. inserisci una scelta valita")


if __name__ == "__main__":
    
    main()