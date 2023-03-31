from ui.ui_main_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget
from widget.diagram_widget import DiagramWidget
from widget.inference_rule_widget import InferenceRuleWidget

class MainWindow(QMainWindow, Ui_MainWindow):
   def __init__(self, pickled=False):
      super().__init__()
      super().__init__()
      self.setupUi(self)
      
      if not pickled:
         self.finish_setup()
         
   def finish_setup(self):
      self.actionNewDiagram.triggered.connect(lambda b: self.add_new_blank_diagram())
      self.actionNewRule.triggered.connect(lambda b: self.add_new_inference_rule())
      
   def add_new_blank_diagram(self):
      pass
   
   def add_new_inference_rule(self):
      inference_rule = InferenceRuleWidget()
      self.centralTabs.addTab(inference_rule, "My Inference Rule (TODO)")