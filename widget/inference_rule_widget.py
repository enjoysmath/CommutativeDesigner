from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget
from ui.ui_inference_rule_widget import Ui_InferenceRuleWidget
from widget.diagram_widget import DiagramWidget
from PyQt5.QtCore import QSize

class InferenceRuleWidget(QWidget, Ui_InferenceRuleWidget):
   Givens, Results = range(2)
   
   def __init__(self, pickled=False):
      super().__init__()
      super().__init__()
      self.setupUi(self)
      self._components = (self.givensList, self.resultsList)
      
      if not pickled:
         self.finish_setup()
      
   def add_given(self, diagram:DiagramWidget):
      self.add_diagram(diagram, component=self.Givens)
      
   def add_diagram(self, diagram:DiagramWidget, component:int):
      component:QListWidget = self._components[component]
      item = QListWidgetItem(component)
      component.addItem(item)
      component.setItemWidget(item, diagram)   
      size = diagram.size()
      size.setWidth(2*size.width())
      item.setSizeHint(size)
      
   def add_result(self, diagram:DiagramWidget):
      self.add_diagram(diagram, component=self.Results)
      
   def finish_setup(self):
      self.add_given(DiagramWidget())
      