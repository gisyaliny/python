from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QMainWindow,QPushButton,QLabel,QGridLayout,QApplication,QLineEdit,QComboBox
from PyQt6.QtGui import QIcon

class Window(QMainWindow):    
    def __init__(self) -> None:
        super().__init__()
        self.clicked_times = 0
        
        self.setMinimumSize(300,300)
        
        grid_layout = QGridLayout()
        self.label = QLabel("This is a label",alignment = Qt.AlignmentFlag.AlignCenter)
        self.btn = QPushButton("Click Me!")
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Please Enter your last name")
        self.comboBox = QComboBox()
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Green")
        self.comboBox.addItem("Yellow")
        self.comboBox.addItem(QIcon("./asset/utd.jpg"),"UTD")
             
        self.btn.clicked.connect(self.clickHandler)
        self.lineEdit.textChanged.connect(self.textChangeHandler)
        self.lineEdit.setMaxLength(10)
        self.comboBox.currentTextChanged.connect(self.comboChange)          
        
        grid_layout.addWidget(self.label,0,0)
        grid_layout.addWidget(self.comboBox,1,0)
        grid_layout.addWidget(self.lineEdit,2,0)
        grid_layout.addWidget(self.btn,3,0)
        centerWidget = QWidget()
        centerWidget.setLayout(grid_layout)
        
        self.setCentralWidget(centerWidget)
        
    def clickHandler(self):
        print("Button clicked!")
        self.clicked_times += 1 
        self.label.setText(f"Button has Been Clicked {self.clicked_times} times!")
        
    def textChangeHandler(self):
        self.label.setText(f"Your last name is {self.lineEdit.text()}")
        
    def comboChange(self):
        self.label.setText(f"Current Combo Box text is {self.comboBox.currentText()}")
        

app = QApplication([])

window = Window()

window.show()

app.exec()



