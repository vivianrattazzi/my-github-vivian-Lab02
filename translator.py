import dictionary as d


class Translator:
    def __init__(self, dizionario):
        self.dizionario = dizionario

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("--------------------------")
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3.Cerca con wildcard\n4.Exit")
        print("--------------------------")


    def loadDictionary(self, dict):

        # dict is a string with the filename of the dictionary
        #dict è il nome del dizionario, quindi questa funzione legge e restituisce tutto il dizionario
        filename = open(dict, 'r')
        contenutoFile = filename.read()
        riga = contenutoFile.split("\n")
        contenutoriga = riga.split(" ")
        self.dizionario[contenutoriga[0]] = contenutoriga[1]

        return self.dizionario


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parole = entry.split(" ")
        parolaAliena = parole[0]
        traduzione = parole[1]
        d.Dictionary.addWord(parolaAliena, traduzione)
        #dictionary.addWord(parolaAliena, traduzione)



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        #qui mi passa la parola aliena e restituisco la traduzione
        d.Dictionary.translate(query)



    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass