import openai
import json
import os
import shutil
from Whisper import AudioRecorderApp
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

    def submit_message(self, output, input,temp,tokens):
        
        request = input.toPlainText()
        input.clear()
        output.append("\n" + "\n" + "User: " + request)
        request_data = {'role': 'user', 'content': request}
        self._add_to_json_file(self.temp_file_path, request_data)
        request_file_path = self.temp_file_path
        self.response_thread = chatCompletion(request_file_path,temp=temp,maxtkns=tokens)
        self.response_thread.responseChanged.connect(lambda response: self._update_output(response, output))
        self.response_thread.start()



    def _update_output(self, response, output):
       if response==" \n \n ERREUR LORS DE LA COMPLETION ESSAYEZ RENVOYER LE MESSAGE SI LE PROBLÉME PERSISTE VERIFIEZ 'ETAT DE LA CONNECTION ET REDEMARREZ L'APPLICATION ":
            output.append("\n" + "\n" + "Betsy: " + response)
       else:
            response_data = {'role': 'assistant', 'content': response}
            self._add_to_json_file(self.temp_file_path, response_data)
            output.append("\n" + "\n" + "Betsy: " + response)

    def _update_input(self, response, input):
            input.append(response)



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
            
 
    def save_Bot(self):
        box = EnregistrerDialog()
 
        box.StartApp()
    
    def transcript(self,dialogwindow,destination):
            window = AudioRecorderApp(destination)
            window.exec_()
    




from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class EnregistrerDialog():
    def __init__(self):
        self.dial = QDialog()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Enregistrer la Séance de travail")
        Dialog.resize(476, 223)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(171, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.pushButton_2.clicked.connect(self.save_context)
        self.pushButton.clicked.connect(self.dial.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enregistrer la Séance de travail"))
        self.label_2.setText(_translate("Dialog", "Entrer le nom du contexte"))
        self.pushButton_2.setText(_translate("Dialog", "Enregister"))
        self.pushButton.setText(_translate("Dialog", "Annuler"))
    
    def save_context(self):
        root = Engine()
        print("saving...")
        sett = root._json_load(root.temp_file_path)
        contextname = self.lineEdit.text()
        if contextname!="":
            print("saving...")
            with open("BetsyApp/contexts/"+contextname+".json","w") as savings:
                json.dump(sett,savings)
                print("saved !")
                self.dial.close()
        else:
            self.label.setText( "...Entrez un nom pour le contexte...")   
                
    
        
    def StartApp(self):
        self.setupUi(Dialog=self.dial)
        self.dial.exec_()
         
        
        
    
        
            

        




    