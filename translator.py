from dictionary import Dictionary

class Translator:
    def __init__(self, dict = Dictionary()):
        self.dict = dict

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Stampa tutto il dizionario
        # 5. Exit
        print("--------------------------")
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3.Cerca con wildcard\n4.Stampa tutto il dizionario\n5.Exit")
        print("--------------------------")


    def loadDictionary(self, file):

        # dict is a string with the filename of the dictionary
        #dict è il nome del dizionario, quindi questa funzione legge e restituisce tutto il dizionario
        return self.dict.popolaDizionario(file)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parole = entry.split(" ") #parole è una lista con parola aliena nella prima posizione e una lista di traduzioni
        parolaAliena = parole[0]
        traduzioni = []
        for i in range(1, len(parole)):
            traduzioni.append(parole[i])

        print(self.dict.addWord(parolaAliena, traduzioni))




    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        #qui mi passa la parola aliena e restituisco la traduzione

       return self.dict.translate(query)




    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        print(self.dict.translateWordWildCard(query))