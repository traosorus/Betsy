import openai
import json
import os
import shutil
import time
import threading
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Engine :
    # Fonction de Chatcompletion d'openAI
    def chatCompletion(self, context):

        openai.api_key = "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"
        self.context = self.jsonload(filename=context)
        self.completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response = str(self.completion.choices[0].message["content"])        
        return response
    

    
    def submit_message(self,output,input):
        request = input.toPlainText()
        input.clear()
        output.append("User: " + request)
        # Extraire la requête la mettre sous format Dict Ajouter au ficher temporaire réécrire sur le outpout supprimer le input
        request = {'role': 'user', 'content': request}
        self.add_to_json_file("contexts/Temporary.json", request)
        reque = "contexts/Temporary.json"
        
        # Envoi de la requête à l'API
   
        try:
            reponse = self.chatCompletion(reque)
            resp = {'role': 'assistant', 'content': reponse}
            self.add_to_json_file("contexts/Temporary.json", resp)
            output.append("\n" + "\n"+"Betsy: "+reponse)
        except:
            with open("contexts/Temporary.json","r") as df:
             historique = json.load(df)
             del historique[:10]
             with open("contexts/Temporary.json","w") as dff:
                json.dump(historique, dff)
                reponse = " \n \n ERREUR LORS DE LA COMPLETION ESSAYEZ RENVOYER LE MESSAGE SI LE PROBLÉME PERSISTE VERIFIEZ 'ETAT DE LA CONNECTION ET REDEMARREZ L'APPLICATION "
                output.append("\n" + "\n"+reponse)
    def submit_message_threaded(self,input,output):
        # Create a new thread to run the submit_message() method
        thread = threading.Thread(target=self.submit_message(input,output))
        thread.start()
        
        

        

    
 # Initialisation de l'environement de travail----------------------------------------------------------------------------------
    
    # Initialisation de la liste des contextes
    def context_list(self):
        
        dossier = "contexts"

        # Initialiser le tableau
        fichiers = []

        # Parcourir tous les fichiers dans le dossier
        for nom_fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, nom_fichier)
            # Vérifier si le fichier est un fichier et pas un dossier
            if os.path.isfile(chemin_fichier) and chemin_fichier != "contexts/Temporary.json":
                # Ajouter le chemin du fichier au tableau
                fichiers.append(str(chemin_fichier))

        return fichiers   
     
    def get_selected_value(self,system,input,output,choice):
        input.clear()
        output.clear()
        system.clear()
        self.__init__Temporary(choice)
        self.galimatia(system=system)
    
    #initialisation du contexte initial   
    def __init__Temporary(self, choice):
        # Afficher le tableau des fichiers
        shutil.copy(choice, "contexts/Temporary.json")

    #initialisation des dossiers et fichiers de running
    @classmethod
    def _init__folders(self):
        self.path= os.path.expanduser("~")
        self.desktop_path = self.path+"/Desktop"
        self.kernel_path= self.desktop_path+"/ChatbotAssistant"
        self.code_path= self.desktop_path+"/ChatbotAssistant/Codes"
        
        try:
            os.mkdir(self.kernel_path)
            os.mkdir(self.code_path)
        except FileExistsError:
            print(" Do Pass")
        with open(self.code_path+"/test.txt", 'a') as cash:
                cash.write("")
                
 # Outils BackEnD----------------------------------------------------------------------------------------------------
    def galimatia(self,system):
        with open("contexts/Temporary.json", "r") as f:
            # Charger les données JSON existantes
            json_data = json.load(f)
            json_data = json_data[0]

        if json_data.get("role") == "system":
            json_data = json_data.get("content")
            system.append(json_data)
        else:
            system.append("Hello i'm your assistant")
    def jsonload (self,filename):
            # Open the JSON file and load its contents into a variable
            with open(filename) as f:
                data = json.load(f)
            return data
    def add_to_json_file(self, file_path, data):
        # Ouvrir le fichier en mode lecture
        with open(file_path, "r") as f:
            # Charger les données JSON existantes
            json_data = json.load(f)

        # Ajouter les nouvelles données à la liste existante
        json_data.append(data)

        # Ouvrir le fichier en mode écriture et écrire les nouvelles données
        with open("contexts/Temporary.json", "w") as f:
            json.dump(json_data, f)

    def extract(self):
      
        with open(self.code_path+"/test.txt", 'r') as file:
            self.code = file.read()
            print(self.code)
        
        print("ok2")
        code_blocks = []
        start = 0
        print("ok4")

        while True:
            start = self.code.find('```python', start)
            if start == -1:
                print("ok5ppp")
                break
            print("ok5")

            end = self.code.find('```', start + 1)
            if end == -1:
                break

            code_block = self.code[start + 10:end].strip()
            code_blocks.append(code_block)
            start = end
            print("ok5")



            with open(self.code_path+"/Betsy.py", "w") as f:
                f.write(code_block)
                
            self.Runcode.insert(END,code_block)
    
    def Updatelist(self):
        self.options = self.context_list()
        self.combo_box.configure(values=self.options)
    

