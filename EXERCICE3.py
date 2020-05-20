from PySide2.QtWidgets import *

class Click(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.nbclick = 0
        self.layout = QVBoxLayout()
        self.setMinimumSize(500, 500)
        self.setWindowTitle('IHM')

        self.button = QPushButton("Changer mon texte !")
        self.textEdit = QTextEdit()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.textEdit)

        self.button.clicked.connect(self.change)


        self.setLayout(self.layout)
    #def fermeture (self):
        #self.close()

    #def change(self):
        #self.textEdit.setText('click'+str(self.nbclick))
       #self.nbclick+=1
    def change(self):
        self.button.setText('click'+str(self.nbclick))
        print(self.nbclick)
        self.textEdit.setText('click'+str(self.nbclick))
        self.nbclick+=1


if __name__ == "__main__":
   app = QApplication([])
   win = Click()
   win.show()
   app.exec_()
