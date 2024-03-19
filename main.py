import translator as tr
t = tr.Translator()
file = 'dictionary.txt'

while(True):

    t.printMenu()

    t.loadDictionary(file)

    txtIn = input("Inserisci un opzione: ")

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txt = input("Scrivi qui: ")

        parolaDaAggiungere = txt.replace(" ", "")
        if parolaDaAggiungere.isalpha():
            t.handleAdd(txt.lower())
            print("Aggiunta!")

    if int(txtIn) == 2:
        print("Ok, di quale parola vuoi conoscere la traduzione?")
        txt = input("Scrivi qui: ")
        if txt.isalpha():
            print(t.handleTranslate(txt.lower()))

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        txt = input("Scrivi qui: ")
        t.handleWildCard(txt)

    if int(txtIn) == 4:
        print(t.loadDictionary(file))

    if int(txtIn) == 5:
        break
