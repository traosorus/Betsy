import openai
import json
from PyQt5.QtCore import QThread,pyqtSignal



class chatCompletion(QThread):
    responseChanged = pyqtSignal(str)
    with open("/Users/m2/Documents/GitHub/Betsy/API_key.txt","r") as key:
        API_key = key.read() 

    def __init__(self, context, maxtkns,temp):
        super().__init__()
        self.context = context
        self.tokens = maxtkns
        self.temp = temp
        self._response = None

    def run(self):
        with open("/Users/m2/Documents/GitHub/Betsy/API_key.txt","r") as key:
            API_key = key.read() 
            print(API_key)
        openai.api_key = API_key
        with open(self.context) as f:
            messages = json.load(f)
        try:      
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=self.temp,
                max_tokens=self.tokens,
                
                )
            self._response = str(completion.choices[0].message["content"])
            self.responseChanged.emit(self._response)
        except:
            print("Fichier plein")
            with open("BetsyApp/contexts/Temporary.json","r") as temp:
                    data = json.load(temp)
                    # Supprimer les 10 premiers éléments
                    data = data[10:]

                # Écrire la nouvelle structure de données dans le fichier JSON
                    with open("BetsyApp/contexts/Temporary.json","w") as temp:
                        json.dump(data, temp)
                        self._response = "Appuyez de nouveau sur envoyer"
                        self.responseChanged.emit(self._response)
            



    @property
    def response(self):
        return self._response