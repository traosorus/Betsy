# Import des modules nécessaires
from Betsy import BetsyGUI
from PyQt5 import QtWidgets
from Betsy_root import Engine
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

# Définition de la classe BetsyApp qui va encapsuler notre application
class BetsyApp:
    # Initialisation de l'application
    def __init__(self):
        # Initialisation de l'application PyQt
        self.app = QtWidgets.QApplication(sys.argv)
        # Initialisation de l'interface graphique BetsyGUI
        self.ui = BetsyGUI()
        # Initialisation du moteur de traitement Engine
        self.engine = Engine()
        # Initialisation de l'interface utilisateur
        self.init_UI()
        # Lancement de l'application
        self.ui.startApp()

        

    # Initialisation de l'interface utilisateur
    def init_UI(self):
        # Initialisation des dossiers du moteur de traitement Engine
        self.engine._init_folders()
        # Récupération des éléments de l'interface utilisateur
        self.output = self.ui.chatlog
        self.input_entry = self.ui.userentry
        self.system = self.ui.systementry
      
        # Récupération de la liste des contextes disponibles dans le moteur de traitement Engine
        context_list = self.engine.context_list()
        # Ajout de la liste des contextes à la combobox de l'interface utilisateur
        self.ui.comboBox.addItems(context_list)
        

        # Définition de la fonction qui sera appelée lors de l'appui sur le bouton "Envoyer"
        def submit():
            self.engine.submit_message(input=self.input_entry, output=self.output)

        # Définition de la fonction qui sera appelée lors de la création d'un nouveau workspace
        def new_workspace():
            self.engine.new_bot(input=self.input_entry, output=self.output, system=self.system)
            self.system.setEnabled(True)

        # Définition de la fonction qui sera appelée lors de la sélection d'un contexte dans la combobox
        def get_context():
            self.engine.get_selected_value(input=self.input_entry, output=self.output, system=self.system, choice=self.ui.comboBox.currentText())
        new_workspace()
        # Connexion des signaux de l'interface utilisateur aux fonctions correspondantes
        self.ui.actionNouvelle_seance_de_travail.triggered.connect(new_workspace)
        self.ui.sendButton.clicked.connect(submit)
        self.ui.applyButton.clicked.connect(get_context)

# Vérification que le script est exécuté en tant que programme principal
if __name__ == '__main__':
    # Initialisation de l'application
    app = BetsyApp()
