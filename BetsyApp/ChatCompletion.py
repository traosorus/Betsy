import openai
import json
from PyQt5.QtCore import QThread,pyqtSignal


class chatCompletion(QThread):
    responseChanged = pyqtSignal(str)

    def __init__(self, context):
        super().__init__()
        self.context = context
        self._response = None

    def run(self):
        try:
            openai.api_key = "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"
            with open(self.context) as f:
                messages = json.load(f)
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            self._response = str(completion.choices[0].message["content"])
            self.responseChanged.emit(self._response)
        except:
            with open("BetsyApp/contexts/Temporary.json","r") as df:
             historique = json.load(df)
             del historique[:10]
             with open("BetsyApp/contexts/Temporary.json","w") as dff:
                json.dump(historique, dff)
            self._response = " \n \n ERREUR LORS DE LA COMPLETION ESSAYEZ RENVOYER LE MESSAGE SI LE PROBLÉME PERSISTE VERIFIEZ 'ETAT DE LA CONNECTION ET REDEMARREZ L'APPLICATION "
            self.responseChanged.emit(self._response)

    @property
    def response(self):
        return self._response