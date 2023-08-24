# Import des modules nécessaires
from Betsy_2 import BetsyGUI
from PyQt5 import QtWidgets
from Betsy_root import Engine
from PyQt5 import QtCore, QtGui, QtWidgets
from CtxtGui import Ui_Form
import sys

# Définition de la classe BetsyApp qui va encapsuler notre application
class BetsyApp:
    # Initialisation de l'application
    def __init__(self):
        # Initialisation de l'application PyQt
        self.app = QtWidgets.QApplication(sys.argv)
        # Initialisation de l'interface graphique BetsyGUI
        self.Betsy = BetsyGUI()
        # Initialisation du moteur de traitement Engine
        self.engine = Engine()
        # Initialisation de l'interface utilisateur
        self.init_UI()
        # Lancement de l'application
        self.Betsy.startApp()

        

    # Initialisation de l'interface utilisateur
    def init_UI(self):
        # Initialisation des dossiers du moteur de traitement Engine
        self.engine._init_folders()
        # Récupération des éléments de l'interface utilisateur
        self.output = self.Betsy.chatlog
        self.input_entry = self.Betsy.userentry
        self.system = self.Betsy.systementry
        self.recording = False
      
        # Récupération de la liste des contextes disponibles dans le moteur de traitement Engine
        context_list = self.engine.context_list()
        # Ajout de la liste des contextes à la combobox de l'interface utilisateur
        self.Betsy.comboBox.addItems(context_list)
        self.temp = 0
        self.Betsy.tempSlider.setValue(700)
        self.Betsy.tokenSlider.setValue(250)
        self.token = 0 
        


        # Définition de la fonction qui sera appelée lors de l'appui sur le bouton "Envoyer"
        def submit():
            print(self.token)
            self.temp = self.Betsy.temp_sliderValue/1000
            self.token = self.Betsy.token_sliderValue 
            print(self.token)
            
            self.engine.submit_message(input=self.input_entry, output=self.output, temp=self.temp,tokens=self.token)

        # Définition de la fonction qui sera appelée lors de la création d'un nouveau workspace
        def new_workspace():
            self.engine.new_bot(input=self.input_entry, output=self.output, system=self.system)
            self.system.setEnabled(True)
        
        def save_workspace():
            self.engine.save_Bot()

        # Définition de la fonction qui sera appelée lors de la sélection d'un contexte dans la combobox
        def get_context():
            self.engine.get_selected_value(input=self.input_entry, output=self.output, system=self.system, choice=self.Betsy.comboBox.currentText())
        
        def transcription():
            from PyQt5.QtWidgets import QDialog
            dial = QDialog()

            self.engine.transcript(dial,destination= self.input_entry)
     
        
        def create_context():
            gui = Ui_Form()
            gui.StartApp()
            
       
            
        new_workspace()
        # Connexion des signaux de l'interface utilisateur aux fonctions correspondantes
        self.Betsy.actionEnregistrer_le_seane_de_travail.triggered.connect(save_workspace)
        self.Betsy.actionNouvelle_seance_de_travail.triggered.connect(new_workspace)
        self.Betsy.actionCreer_un_nouveau_contexte.triggered.connect(create_context)
        self.Betsy.sendButton.clicked.connect(submit)
        self.Betsy.applyButton.clicked.connect(get_context)
        self.Betsy.transcript.clicked.connect(transcription)
        

# Vérification que le script est exécuté en tant que programme principal
if __name__ == '__main__':
    # Initialisation de l'application
    app = BetsyApp()