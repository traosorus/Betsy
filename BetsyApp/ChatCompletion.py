import openai
import json
from PyQt5.QtCore import QThread,pyqtSignal


class chatCompletion(QThread):
    responseChanged = pyqtSignal(str)

    def __init__(self, context, maxtkns,temp):
        super().__init__()
        self.context = context
        self.tokens = maxtkns
        self.temp = temp
        self._response = None

    def run(self):
    
        openai.api_key = "API key"
        with open(self.context) as f:
            messages = json.load(f)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=self.temp,
            max_tokens=self.tokens,
            
            )
        
        self._response = str(completion.choices[0].message["content"])
        self.responseChanged.emit(self._response)


    @property
    def response(self):
        return self._response