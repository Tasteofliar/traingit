import maya.cmds as cmds
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import importlib

from.import sphereToolFunct as stfn
importlib.reload(stfn)
class sphereTool(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(sphereTool, self).__init__(*args, **kwargs)
        self.resize(300,100)
        self.setWindowTitle('Polygon Create')
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        self.init_input_widget()
        self.init_opt_widget()
        
        self.main_layout.addWidget(self.main_input_widget)
        self.main_layout.addWidget(self.main_opt_widget)
        
    def init_input_widget(self):
        self.main_input_widget = QWidget()
        self.main_input_layout = QHBoxLayout()
        self.main_input_widget.setLayout(self.main_input_layout)
            
        self.name_label = QLabel('Name :')
        self.name_LineEdit = QLineEdit()
            
        self.amount_label = QLabel('Amount : ')
        self.amount_spinBox = QSpinBox()
        self.amount_spinBox.setMinimum(1)
        self.amount_spinBox.setMaximum(10)
        
        self.main_input_layout.addWidget(self.name_label)
        self.main_input_layout.addWidget(self.name_LineEdit)
        self.main_input_layout.addWidget(self.amount_label)
        self.main_input_layout.addWidget( self.amount_spinBox)
              
    def init_opt_widget(self):
        self.main_opt_widget = QWidget()
        self.main_opt_layout = QHBoxLayout()
        self.main_opt_widget.setLayout(self.main_opt_layout)
        
        self.ok_button = QPushButton("OK")
        self.ok_button.setMinimumHeight(50)
        self.main_opt_layout.addWidget(self.ok_button)
        self.ok_button.clicked.connect(self.doCreateSphere)
        #self.ok_button.clicked.connect(self.getTxt)
        #self.ok_button.clicked.connect(self.getComboItem)
        
        self.no_button = QPushButton("Cancel")
        self.no_button.setMinimumHeight(50)
        self.main_opt_layout.addWidget(self.no_button)
        self.no_button.clicked.connect(self.toolClose)
        
        self.setWindowOpacity(1)

    def toolClose(self):
         self.close()

    def doCreateSphere(self):
         objName = self.name_LineEdit.text()
         amount = self.amount_spinBox.value()
         stfn.createSphere(objName, amount)

global ui

try:
    ui.close()
except:
    pass
        
maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)

ui = sphereTool(parent = ptr)
ui.show()