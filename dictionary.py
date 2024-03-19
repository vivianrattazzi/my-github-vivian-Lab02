
class Dictionary:
    def __init__(self, dict = {}):
        self.dict = dict

    def popolaDizionario(self, file):
        filename = open(file, 'r')
        contenutoFile = filename.read()
        riga = contenutoFile.split("\n")
        for elemento in riga:
            contenutoriga = elemento.split(" ")
            self.dict[contenutoriga[0]] = contenutoriga[1]
        return self.dict




    def addWord(self, parolaAliena, traduzioni):

        for key in self.dict:#se la parola è già contenuta nel dizionario
            if parolaAliena == key:
                for traduzione in traduzioni:
                    self.dict[key].append(traduzione)

                return [key, self.dict[key]]


        self.dict[parolaAliena] = traduzioni#se è la prima volta che la aggiungo
        return [parolaAliena, traduzioni]



    def translate(self, query):
        for key in self.dict:
            if query == key:
                return self.dict[key]

    def translateWordWildCard(self, query):
        posizione = 0
        for i in range(0, len(query)):
            if query[i] == "?":
                posizione = i

        for key in self.dict:
            if len(key) >= posizione:
               nuovaquery = query.replace("?", key[posizione])
               if nuovaquery.lower() == key:
                   return [self.dict[key]]




