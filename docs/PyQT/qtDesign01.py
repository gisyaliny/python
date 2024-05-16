from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QWidget,QMainWindow
import design 

class MyWindow(QMainWindow,design.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.pushBtnHandler)
        
    def pushBtnHandler(self):
        self.listWidget.addItem(self.lineEdit.text())
        self.lineEdit.setText("")
    
app = QApplication([])
window = MyWindow()
window.show()
app.exec()