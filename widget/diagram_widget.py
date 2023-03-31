from ui.ui_diagram_widget import Ui_DiagramWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl, pyqtSignal
import os

class DiagramWidget(QWidget, Ui_DiagramWidget):
   mouse_pressed = pyqtSignal()
   
   def __init__(self):
      super().__init__()
      super().__init__()
      self.setupUi(self)
      self.webEngineView.load(QUrl.fromLocalFile(os.path.abspath('./test.html')))
      
   def mousePressEvent(self, event):
      self.mouse_pressed.emit()
      super().mousePressEvent(event)
      
      
      
      