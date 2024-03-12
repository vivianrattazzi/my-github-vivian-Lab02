import translator as t

class Dictionary:
    def __init__(self, dizionario):
        self.dizionario = dizionario

    def popolaDizionario(self):#l'ho creata io
       self.dizionario = t.Translator.loadDictionary(dict)

    def addWord(self, parolaAliena, traduzione):
        self.dizionario[parolaAliena] = traduzione

    def translate(self, query):
        for key in self.dizionario:
            if query == key:
                return self.dizionario[key]

    def translateWordWildCard(self):
        pass

