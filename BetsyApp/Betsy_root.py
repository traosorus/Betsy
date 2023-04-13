import openai
import json
import os
import shutil
import time
import threading
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QEventLoop, QTimer, QThread
import sys
from ChatCompletion import chatCompletion



class Engine:
    def __init__(self):
        self.api_key = "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"
        self.model = "gpt-3.5-turbo"
        self.temp_file_path = "BetsyApp/contexts/Temporary.json"
        self.contexts_dir = "BetsyApp/contexts"
        self.path = os.path.expanduser("~")
        self.desktop_path = self.path + "/Desktop"
        self.kernel_path = self.desktop_path + "/ChatbotAssistant"
        self.code_path = self.desktop_path + "/ChatbotAssistant/Codes"
        self._init_folders()

    def _init_folders(self):
        try:
            os.mkdir(self.kernel_path)
            os.mkdir(self.code_path)
        except FileExistsError:
            pass
        with open(self.code_path + "/test.txt", 'a') as cash:
            cash.write("")

    def chat_completion(self, context):
        openai.api_key = self.api_key
        context_data = self._json_load(filename=context)
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=context_data
        )
        response = str(completion.choices[0].message["content"])
        return response

    def submit_message(self, output, input):
        
        request = input.toPlainText()
        input.clear()
        output.append("\n" + "\n" + "User: " + request)
        request_data = {'role': 'user', 'content': request}
        self._add_to_json_file(self.temp_file_path, request_data)
        request_file_path = self.temp_file_path
        self.response_thread = chatCompletion(request_file_path)
        self.response_thread.responseChanged.connect(lambda response: self._update_output(response, output))
        self.response_thread.start()



    def _update_output(self, response, output):
       if response==" \n \n ERREUR LORS DE LA COMPLETION ESSAYEZ RENVOYER LE MESSAGE SI LE PROBLÉME PERSISTE VERIFIEZ 'ETAT DE LA CONNECTION ET REDEMARREZ L'APPLICATION ":
            output.append("\n" + "\n" + "Betsy: " + response)
       else:
            response_data = {'role': 'assistant', 'content': response}
            self._add_to_json_file(self.temp_file_path, response_data)
            output.append("\n" + "\n" + "Betsy: " + response)



    def context_list(self):
        files = [os.path.join(self.contexts_dir, name) for name in os.listdir(self.contexts_dir)
                 if os.path.isfile(os.path.join(self.contexts_dir, name)) and
                 os.path.join(self.contexts_dir, name) != self.temp_file_path]
        return files

    def get_selected_value(self, system, input, output, choice):
        input.clear()
        output.clear()
        system.clear()
        self._init_temporary(choice)
        self._galimatia(system=system)

    def _init_temporary(self, choice):
        shutil.copy(choice, self.temp_file_path)

    def new_bot(self, input, output, system):
        output.setEnabled(True)
        input.setEnabled(True)
        system.setEnabled(True)
        system.clear()
        input.clear()
        output.clear()
        system.setEnabled(False)
        with open(self.temp_file_path, "w") as f:
            json.dump([{"role": "system", "content": " Sarcastic assistant !"}], f)
        self._galimatia(system=system)

    def _galimatia(self, system):
        with open(self.temp_file_path, "r") as f:
            json_data = json.load(f)
            json_data = json_data[0]
        if json_data.get("role") == "system":
            json_data = json_data.get("content")
            self.animate_text(destination=system,text=json_data,delay=0.3)
        else:
            system.append("Hello i'm your assistant")

    def _json_load(self, filename):
        with open(filename) as f:
            data = json.load(f)
        return data

    def _add_to_json_file(self, file_path, data):
        with open(file_path, "r") as f:
            json_data = json.load(f)
        json_data.append(data)
        with open(file_path, "w") as f:
            json.dump(json_data, f)

    def update_list(self, combo_box):
        options = self.context_list()
        combo_box.configure(values=options)

    def animate_text(self, destination, text, delay):
        self.text = list(text)
        self.timer = QTimer()
        self.timer.setInterval(int(delay*100))
        self.timer.timeout.connect(lambda: self.update_text(destination))
        self.timer.start()

    def update_text(self, destination):
        if len(self.text) > 0:
            destination.insertPlainText(self.text[0])
            destination.ensureCursorVisible()
            self.text.pop(0)
        else:
            self.timer.stop()
            
class MonThread(QThread):
    def __init__(self,inp,out,lemos):
        super(MonThread, self).__init__()
        self.output= out
        self.input= inp
        self.lemos = lemos

    def run(self):
        """Code exécuté dans le thread"""
        print("Le thread a commencé.")
        self.lemos.submit_message(output=self.output,input=self.input)
        time.sleep(5)
        print("Le thread a terminé.")
        




    