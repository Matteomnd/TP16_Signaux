from PySide2.QtWidgets import *

class toolBarre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.setWindowTitle('IHM')

        self.progressBar = QProgressBar()
        self.slider = QSlider()

        self.layout.addWidget(self.progressBar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.progression)

        self.setLayout(self.layout)


    def progression(self):
        valeur = self.slider.value()
        self.progressBar.setValue(valeur)



if __name__ == "__main__":
   app = QApplication([])
   win = toolBarre()
   win.show()
   app.exec_()
