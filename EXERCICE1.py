from PySide2.QtWidgets import *
import random

class Signal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout= QVBoxLayout()

        self.setMinimumSize(500, 500)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.button = QPushButton("Changer le cycle")
        self.label = QLabel('CSI')

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.switched)
        self.setLayout(self.layout)


    def switched(self):
        list_cycles= ["CSI","CIR","BIOST","CENT","BIAST","EST"]
        cycles= random.choice(list_cycles)
        self.label.setText(cycles)



if __name__ == "__main__":
   app = QApplication([])
   win = Signal()
   win.show()
   app.exec_()
