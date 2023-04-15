import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Bubble(QtWidgets.QWidget):
    def __init__(self, message, incoming=True):
        super().__init__()
        self._incoming = incoming
        self._message = message
        self._color = QtGui.QColor("#DCF8C6") if incoming else QtGui.QColor("#E3E3E3")
        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._text = QtWidgets.QLabel(self._message)
        self._text.setWordWrap(True)
        self._text.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self._text.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self._text.setMargin(10)
        self._text.setContentsMargins(0, 0, 0, 0)
        self._text.setStyleSheet("QLabel {{ background-color: {color}; border-radius: 15px; }}".format(color=self._color.name()))
        self._layout.addWidget(self._text)
        if self._incoming:
            self._layout.setAlignment(QtCore.Qt.AlignLeft)
        else:
            self._layout.setAlignment(QtCore.Qt.AlignRight)

    def sizeHint(self):
        max_bubble_width = 33 # max width of the bubble based on the screen size
        font = self._text.font()
        fontMetrics = QtGui.QFontMetrics(font)
        textWidth = fontMetrics.boundingRect(self._text.text()).width() # total text width
        num_lines = self._message.count('\n') + 1 # count number of lines in the text
        textHeight = fontMetrics.boundingRect(" ").height() * num_lines  # total text height
        if textWidth > max_bubble_width: # adjust width to max_bubble_width
            textWidth = max_bubble_width
        return QtCore.QSize(textWidth + 20, textHeight + 20) 
    
class ChatBot(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        # Calcul des dimensions de la fenêtre en pourcentage
        screenGeometry = QtWidgets.QApplication.desktop().availableGeometry()
        windowWidth = int(screenGeometry.width() * 0.25)  # 25% de la largeur de l'écran
        windowHeight = int(screenGeometry.height() * 0.7)  # 70% de la hauteur de l'écran

        self.setSizeIncrement(windowWidth, windowHeight)
        self.move(int(screenGeometry.width() * 0.375), int(screenGeometry.height() * 0.15))  # centrer la fenêtre

        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._scrollArea = QtWidgets.QScrollArea(self)
        self._scrollArea.setWidgetResizable(True)
        self._scrollAreaContents = QtWidgets.QWidget(self._scrollArea)
        self._scrollAreaContentsLayout = QtWidgets.QVBoxLayout(self._scrollAreaContents)
        self._scrollArea.setWidget(self._scrollAreaContents)
        self._layout.addWidget(self._scrollArea)
        self._inputLayout = QtWidgets.QHBoxLayout()
        self._inputLayout.setContentsMargins(10, 10, 10, 10)
        self._inputField = QtWidgets.QLineEdit(self)
        self._inputLayout.addWidget(self._inputField)
        self._sendButton = QtWidgets.QPushButton("Send", self)
        self._sendButton.clicked.connect(self.sendMessage)
        self._inputLayout.addWidget(self._sendButton)
        self._layout.addLayout(self._inputLayout)

    def sendMessage(self):
        message = self._inputField.text()
        if message:
            bubble = Bubble(message, False)
            self._scrollAreaContentsLayout.addWidget(bubble)
            self._inputField.setText("")
            reply = self.getReply(message)
            if reply:
                replyBubble = Bubble(reply, True)
                self._scrollAreaContentsLayout.addWidget(replyBubble)

    def getReply(self, message):
        # Cette méthode doit être remplacée par le code qui traite le message et retourne la réponse du chatbot
        # Dans cet exemple, le chatbot renvoie simplement un message de réponse aléatoire
        # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
        import openai
        openai.api_key = "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"
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
               
            ]
        )
        return str(completion.choices[0].message["content"])
    
        



# Point d'entrée du programme
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ChatBot()
    window.show()
    sys.exit(app.exec_())

