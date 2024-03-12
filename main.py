import translator as tr
t = tr.Translator('dizionario')


while(True):

    t.printMenu()

    #t.loadDictionary("")

    txtIn = input("Inserisci un opzione: ")

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input("Scrivi qui: ")
        parolaAggiunta = txtIn.lower()
        t.handleAdd(parolaAggiunta)

    if int(txtIn) == 2:
        print("Ok, di quale parola vuoi conoscere la traduzione?")
        txtIn = input("Scrivi qui: ")
        parolaAliena = txtIn.lower().strip()
        if parolaAliena.isalpha():#mi assicuro di avere solo caratteri alfabetici
        #metto la funzione che mi traduce la parola aliena in italiano
            print(t.handleTranslate(parolaAliena))

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        txtIn = input("Scrivi qui: ")
        pass
    if int(txtIn) == 4:
        break
