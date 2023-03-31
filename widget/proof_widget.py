from PyQt5.QtWidgets import QWidget
from widget.flow_layout import FlowLayout

class ProofWidget(QWidget):
   def __init__(self):
      super().__init__()
      self.setLayout(FlowLayout())
      
   
      