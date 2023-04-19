import tkinter as tk
from tkinter import ttk
from tkinter import *
import openai
import json
import os
import shutil
import time
import threading
import subprocess


# Sorry for the mister Frenglish 

def center_window(window):
    w = 1000
    h = 600

    # get screen width and height
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen 
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


class Create_context_Define_gui():

    def __init__(self, master):

        # Créer la fenêtre principale
        self.root = master
        self.root.title("Créer un nouveau contexte")
        self.root.geometry('%dx%d+%d+%d' % (780, 360, (720 - (780 / 2)), (450 - (360 / 2))))
        self.contexttitle = ""
        self.Body = []
        self.entriesU = []
        self.entriesA = []

        # Créer les labels et les Entry
        label = tk.Label(self.root, text="System" + ": ")
        label.grid(row=0, column=0, padx=5, pady=5)
        self.entry = tk.Text(self.root, height=5, width=50)
        self.entry.grid(row=0, columnspan=4, padx=5, pady=5)

        # Créer le bouton Enregistrer
        save_button = tk.Button(self.root, text="Compile", command=self.save_entries)
        save_button.grid(row=8, column=2, padx=5, pady=5)

        for i in range(3):
            self.labelu = tk.Label(self.root, text=" User: ")
            self.labelu.grid(row=i + 1, column=0, padx=5, pady=5)
            labeluu = tk.Label(self.root, text="Dialogue " + str(i))
            labeluu.grid(row=i + 1, column=4, padx=5, pady=5)
            self.entryu = tk.Text(self.root, height=3, width=25)
            self.entryu.grid(row=i + 1, column=1, padx=5, pady=5)
            self.labela = tk.Label(self.root, text=" Assistant : ")
            self.labela.grid(row=i + 1, column=2, padx=5, pady=5)
            self.entryaa = tk.Text(self.root, height=4, width=25)
            self.entryaa.grid(row=(i + 1), column=3, padx=5, pady=5)
            self.entriesU.append(self.entryu)
            self.entriesA.append(self.entryaa)

    def save_entries(self):

        for i in range(len(self.entriesA)):
            entry1 = {'role': 'user', 'content': self.entriesU[i].get("1.0", END)}
            entry2 = {'role': 'assistant', 'content': self.entriesA[i].get("1.0", END)}
            self.Body.append(entry1)
            self.Body.append(entry2)
        system = {'role': 'system', 'content': self.entry.get("1.0", END)}
        self.Body.insert(0, system)
        self.Title = "ChatBotAssistant V1/contexts/" + self.contexttitle + ".json"
        with open(self.Title, "w") as f:
            json.dump(self.Body, f)
        self.root.destroy()


class chatCompletion:

    # context est un fichier json
    def __init__(self, context):
        openai.api_key = "API KEY"
        self.context = self.jsonload(filename=context)
        self.completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        self.response = str(self.completion.choices[0].message["content"])

    def jsonload(self, filename):
        # Open the JSON file and load its contents into a variable
        with open(filename) as f:
            data = json.load(f)
        return data


class ChatbotGUI:

    def gui(self, master):
        self.__init__folders()
        self.master = master
        self.master.title("Chatbot")
        center_window(self.master)

        # Create chat log frame
        self.chat_frame = tk.LabelFrame(master, text="Assistant virtuel")
        self.chat_frame.pack(side=tk.LEFT, padx=20)

        # Create chat log text widget
        self.chat_log = tk.Text(self.chat_frame, height=20, width=80, state=DISABLED)
        self.chat_log.pack(side=tk.TOP,pady=15,padx=10)

        # Create input frame
        self.input_frame = tk.LabelFrame(master, text="SYSTEM")
        self.input_frame.pack(side=tk.TOP, padx=10, pady=10)
        # Add input widget to input frame
        self.systemEntry = tk.Text(self.input_frame, height=12, width=30)
        self.systemEntry.pack(padx=5)

        # Create input label and entry widget
        self.input_label = tk.Label(self.chat_frame, text="Enter message:")
        self.input_label.pack(side=tk.TOP, pady=5)
        self.input_entry = tk.Text(self.chat_frame, height=4, width=50, state=DISABLED)

        self.input_entry.pack(side=tk.TOP)

        # Create submit button
        self.submit_button = tk.Button(self.chat_frame, text="Submit", command=self.submit_message_threaded)
        self.submit_button.pack(side=tk.TOP, pady=10)

        # Crée une liste déroulante avec trois options
        # Créez une variable de type StringVar pour stocker la valeur sélectionnée dans le Combobox
        self.selected_value = tk.StringVar()

        self.options = self.context_list()

        self.combo_box = ttk.Combobox(self.input_frame, textvariable=self.selected_value, values=self.options)
        self.selected_value.set("ChatBotAssistant V1/contexts/Default.json")
        self.combo_box.pack(side=tk.RIGHT, padx=10, pady=10)
        # Fonction pour récupérer la valeur sélectionnée

        self.getcode = tk.Button(master=self.master, text="Get Code", command=self.extract)
        self.getcode.pack()

        # Bouton pour récupérer la valeur sélectionnée
        button = tk.Button(self.input_frame, text="Apply", command=self.get_selected_value)
        button.pack(side=tk.LEFT, pady=10)
        
     

        # Créer une barre de menu
        self.menu_bar = tk.Menu(self.master)

        # Créer une option "Fichier" avec des sous-options
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Nouvelle séance de travail", command=self.New_bot)
        self.file_menu.add_command(label="Recmmencer la sceance de travail", command=self.get_selected_value)
        self.file_menu.add_command(label="Enregistrer la seance de travail", command=self.saveBot)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=self.master.quit)

        # Ajouter l'option "Fichier" à la barre de menu
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.Menucontext = tk.Menu(self.menu_bar, tearoff=0)

        # Ajouter d'autres options à la barre de menu
        self.Menucontext.add_command(label="Créer un ouveau contexte", command=self.Createcontext)
        self.Menucontext.add_command(label="Mettre à jour la Liste des contextes", command=self.Updatelist)
        self.Menucontext.add_command(label="Supprimer un contexte", command=self.Delete_context)
        self.menu_bar.add_cascade(label="contexte", menu=self.Menucontext)
        self.Runcode = tk.Text(self.master,height=30,width=40)
        self.Runcode.pack(pady=10)
        # Configurer la fenêtre pour utiliser la barre de menu
        self.master.config(menu=self.menu_bar)
        self.master.bind("<Button-2>", self.do_popup)

    # -------------------------------------------------------------------Functions----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------Functions----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def get_selected_value(self):
        self.systemEntry.configure(state=NORMAL)
        self.input_entry.delete("1.0", tk.END)
        self.chat_log.delete("1.0", tk.END)
        self.systemEntry.delete("1.0", tk.END)
        value = self.selected_value.get()
        self.__init__Temporary(value)
        self.chat_log.configure(state=NORMAL)
        self.input_entry.configure(state=NORMAL)

        self.galimatia()

    def galimatia(self):
        self.systemEntry.configure(state=NORMAL)
        with open("ChatBotAssistant V1/contexts/Temporary.json", "r") as f:
            # Charger les données JSON existantes
            json_data = json.load(f)
            json_data = json_data[0]

        if json_data.get("role") == "system":
            json_data = json_data.get("content")
            self.animate_text(self.systemEntry, json_data, 0.0000000000000000000001)
        else:
            self.systemEntry.insert(END, "Hello i'm your assistant")
        self.systemEntry.configure(state=DISABLED)

    def animate_text(self, destination, text, delay):
        self.text = destination
        for i in range(len(text)):
            destination.insert(tk.END, text[i])
            destination.see("end")
            self.master.update()
            time.sleep(delay)

    def Createcontext(self):

        # création d'un nouvel objet context
        Context_gui_init_ = Toplevel()
        new = Create_context_Define_gui(Context_gui_init_)
        new.root.iconify()

        def getentryctx():
            new.contexttitle = previewnetry.get()
            self.preview.destroy()
            new.root.deiconify()

        # Preview Choix du context
        self.preview = Toplevel()
        self.preview.geometry('%dx%d+%d+%d' % (300, 200, 570, 350))
        previewLabel = tk.Label(master=self.preview, text="Entrez le nom du contexte")
        previewnetry = tk.Entry(master=self.preview, )
        previewnetry.pack()
        previewLabel.pack()
        getcontexttitle = tk.Button(master=self.preview, text="Valider", command=getentryctx)
        getcontexttitle.pack()
        
    def submit_message(self):
        
        # Get input message and add it to chat log
        requests = self.input_entry.get("1.0", tk.END)
        request = {'role': 'user', 'content': requests}
        self.add_to_json_file("ChatBotAssistant V1/contexts/Temporary.json", request)
        reque = "ChatBotAssistant V1/contexts/Temporary.json"
        self.chat_log.insert(tk.END, "\n" + "\n"+ "\n")

        self.chat_log.insert(tk.END, "User: " + requests)
        self.input_entry.delete("1.0", tk.END)

        # Send message to chatbot and add self.response to chat log
        self.response = self.send_message_to_chatbot(reque)
        self.mordicus = self.response
        self.chat_log.insert(tk.END, "\n" + "\n")
        self.animate_text(destination=self.chat_log,text="Betsy_AI : "+self.response,delay=0.0000000000000000000001)
        with open(self.code_path+"/test.txt", "w") as z:
            z.write(self.response)
        # Clear input entry widget

        
    def submit_message_threaded(self):
        # Create a new thread to run the submit_message() method
        thread = threading.Thread(target=self.submit_message)
        thread.start()

        
    def send_message_to_chatbot(self, message):
        try:
            # Code for sending message to chatbot and getting self.response
            self.response = chatCompletion(message)
            resp = {'role': 'user', 'content': self.response.response}
            self.add_to_json_file("ChatBotAssistant V1/contexts/Temporary.json", resp)
            answer= self.response.response
        except:
            with open("ChatBotAssistant V1/contexts/Temporary.json","r") as df:
             historique = json.load(df)
             del historique[:10]
             with open("ChatBotAssistant V1/contexts/Temporary.json","w") as dff:
                json.dump(historique, dff)
                answer = " \n \n ERREUR LORS DE LA COMPLETION ESSAYEZ RENVOYER LE MESSAGE SI LE PROBLÉME PERSISTE VERIFIEZ 'ETAT DE LA CONNECTION ET REDEMARREZ L'APPLICATION "

        return answer


    def add_to_json_file(self, file_path, data):
        # Ouvrir le fichier en mode lecture
        with open(file_path, "r") as f:
            # Charger les données JSON existantes
            json_data = json.load(f)

        # Ajouter les nouvelles données à la liste existante
        json_data.append(data)

        # Ouvrir le fichier en mode écriture et écrire les nouvelles données
        with open("ChatBotAssistant V1/contexts/Temporary.json", "w") as f:
            json.dump(json_data, f)

    def New_bot(self):
        self.chat_log.configure(state=NORMAL)
        self.input_entry.configure(state=NORMAL)
        self.systemEntry.configure(state=NORMAL)
        self.systemEntry.delete("1.0", tk.END)
        self.systemEntry.configure(state=DISABLED)

        # Ouvrir le fichier en mode écriture et écrire les nouvelles données
        with open("ChatBotAssistant V1/contexts/Temporary.json", "w") as f:
            json.dump([{"role": "system", "content": "You are a sarcastic assistant"}], f)
        self.selected_value.set("ChatBotAssistant V1/contexts/Default.json")
        self.galimatia()

    def saveBot(self):
        save = Toplevel()
        Chat_name_entry = tk.Entry(master=save, width=25)
        Chat_name_Label = tk.Label(master=save, text="Choisissez un nom pour ce chat")
        Chat_name_entry.pack()
        Chat_name_Label.pack()

        def save_context():
            chat_name = Chat_name_entry.get()
            if not chat_name:
                return  # ne pas sauvegarder s'il n'y a pas de nom entré

            os.makedirs("contexts", exist_ok=True)  # créer le répertoire s'il n'existe pas

            temp_file = "ChatBotAssistant V1/contexts/Temporary.json"
            save_file = f"ChatBotAssistant V1/contexts/{chat_name}.json"

            with open(temp_file, "r") as f:
                data = json.load(f)

            with open(save_file, "w") as f2:
                json.dump(data, f2)

            save.destroy()  # fermer la fenêtre de dialogue

        save_button = tk.Button(master=save, text="Enregistrer", command=save_context)
        save_button.pack()

    def context_list(self):
        # Définir le dossier à répertorier
        dossier = "ChatBotAssistant V1/contexts"

        # Initialiser le tableau
        fichiers = []

        # Parcourir tous les fichiers dans le dossier
        for nom_fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, nom_fichier)
            # Vérifier si le fichier est un fichier et pas un dossier
            if os.path.isfile(chemin_fichier) and chemin_fichier != "ChatBotAssistant V1/contexts/Temporary.json":
                # Ajouter le chemin du fichier au tableau
                fichiers.append(str(chemin_fichier))

        return fichiers

    def __init__Temporary(self, choice):
        # Afficher le tableau des fichiers
        shutil.copy(choice, "ChatBotAssistant V1/contexts/Temporary.json")

    # MacOS change '/' with '\' for windows
    def __init__folders(self):
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
        
    def Delete_context(self):
        files = self.context_list()

        delroot = Toplevel()

        # Create Combobox to display files for deletion
        combobox = ttk.Combobox(delroot, state="readonly")
        combobox["values"] = files
        combobox.pack()

        def delete_value():
            value = combobox.get()
            try:
                os.remove(value)
            except:
                pass
            delroot.destroy()

        # Create delete button to initiate the delete confirmation process
        delete_button = tk.Button(delroot, text="Delete Selected File", command=delete_value)
        delete_button.pack()
 
    def start_betsy_thread(self):
        # Create a new thread for running Betsy
        betsy_thread = threading.Thread(target=self.run_betsy)
        # Start the thread
        betsy_thread.start()
        
    def do_popup(self,event):
        m = Menu(self.master, tearoff = 0)
        m.add_command(label ="Copier", command=self.copier)
        m.add_command(label ="Coller", command=self.coller)
        m.add_separator()
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()
    def couper(self):
        self.master.clipboard_clear()
        a=self.master.focus_get().index(ANCHOR)
        i=self.master.focus_get().index(INSERT)
        if i<a:a,i=i,a
        t=self.master.focus_get().get()
        s=t[a:i]
        t=t[0:a] + t[i:]
        self.master.focus_get().delete(0,END)
        self.master.focus_get().insert(0, t)
        self.master.focus_get().icursor(a)
        self.master.clipboard_append(s)
    
    def copier(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.master.selection_get())
    
    def coller(self):
        t=self.master.selection_get(selection='CLIPBOARD')
        self.master.focus_get().insert(INSERT,t) 
# Initialize Tkinter
root = tk.Tk()

# Initialize chatbot GUI
ChatbotGUI().gui(root)


# Start main event loop
root.mainloop()