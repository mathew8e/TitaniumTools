import string
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from rename import bulkRename
from sort import sort, sortWideToTall
from cloneDel import duplicateDelete


class window(QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(400,200)
        self.setWindowTitle("Titanium Image Tools")
        self.label = QLabel(self)
        self.label.setText("Titanium Image Tools")
        font = QFont()
        font.setFamily("Montserrat")
        font.setWeight(500)
        font.setPointSize(16)
        fontSmall = QFont()
        fontSmall.setFamily("Montserrat")
        fontSmall.setWeight(500)
        fontSmall.setPointSize(14)
        
        self.label.setFont(font)
        self.label.move(50,20)
        
        self.label2 = QLabel(self)
        self.label2.setText("path: ")
        self.label2.move(20, 60)
        self.label2.setFont(fontSmall)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(80, 60)
        self.textbox.resize(280, 30)
        
        self.button = QPushButton('Sort into three categories', self)
        self.button.move(20, 110)
        self.button.clicked.connect(lambda:self.buttonAction(self.button))
         
        self.button2 = QPushButton('Sort from tall to wide', self)
        self.button2.move(200, 110)
        self.button2.clicked.connect(lambda:self.buttonAction(self.button2))
        
        self.button3 = QPushButton('Delete duplicate images', self)
        self.button3.move(20, 150)
        self.button3.clicked.connect(lambda:self.buttonAction(self.button3))

        self.button4 = QPushButton('Rename images', self)
        self.button4.move(200, 150)
        self.button4.clicked.connect(lambda:self.buttonAction(self.button4))

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(200, 200)
        self.textbox2.resize(150, 30)

        self.show()

   
    def buttonAction(self, b):
        path = self.textbox.text()
        
        if b.text() == "Sort into three categories":
            exception = sort(path)
            exceptionMessages(exception)
        elif b.text() == "Sort from tall to wide":
            exception = sortWideToTall(path)
            exceptionMessages(exception)
        elif b.text() == "Delete duplicate images":
            exception = duplicateDelete(path)
            exceptionMessages(exception)
        elif b.text() == "Rename images":
            exception = bulkRename(path, self.textbox2.text())
            exceptionMessages(exception)
            
        

def exceptionMessages(exception):
    msg = QMessageBox()
    msg.setWindowTitle("ImgCloneFinderInfo")
    if exception == 1:
        msg.setText("Finished.")
    elif isinstance(exception, str):
        msg.setText(exception)
    else: 
        msg.setText("Something went wrong.")
    
    x = msg.exec_()
    
        
      
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()