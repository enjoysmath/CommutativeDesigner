from ui.ui_diagram_editor_widget import Ui_DiagramEditorWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl, pyqtSignal
import os

class DiagramWidget(QWidget, Ui_DiagramEditorWidget):
   mouse_pressed = pyqtSignal()
   
   def __init__(self):
      super().__init__()
      super().__init__()
      self.setupUi(self)
      self.webEngineView.load(QUrl.fromLocalFile(os.path.abspath('./test.html')))
      
   def mousePressEvent(self, event):
      self.mouse_pressed.emit()
      super().mousePressEvent(event)
      
      
      
