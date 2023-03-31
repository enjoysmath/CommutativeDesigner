import sys
from dialog.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl

#class Example(QWidget):

   #def __init__(self):
      #super().__init__()

      #self.initUI()

   #def initUI(self):

      #vbox = QVBoxLayout(self)

      #self.webEngineView = QWebEngineView()
      #self.loadPage()
      
      #self.button = QPushButton("Press me")
      #self.button.setParent(self)

      #vbox.addWidget(self.webEngineView)
      ##vbox.addWidget(self.button)
      
      #self.button.clicked.connect(lambda: print(self.webEngineView.url().toString()))

      #self.setLayout(vbox)

      #self.setGeometry(300, 300, 350, 250)
      #self.setWindowTitle('QWebEngineView')
      #self.show()

   #def loadPage(self):

      ##with open('index.html', 'r') as f:

         ##html = f.read()
      #self.webEngineView.load(QUrl.fromLocalFile(r'C:\Users\fruit\OneDrive\Desktop\QuiverGames\src\index.html'))

def main():
   app = QApplication([])
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()