# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagram_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiagramWidget(object):
    def setupUi(self, DiagramWidget):
        DiagramWidget.setObjectName("DiagramWidget")
        DiagramWidget.resize(263, 182)
        self.gridLayout = QtWidgets.QGridLayout(DiagramWidget)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(DiagramWidget)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 0, 1, 2, 2)

        self.retranslateUi(DiagramWidget)
        QtCore.QMetaObject.connectSlotsByName(DiagramWidget)

    def retranslateUi(self, DiagramWidget):
        _translate = QtCore.QCoreApplication.translate
        DiagramWidget.setWindowTitle(_translate("DiagramWidget", "Form"))
from PyQt5 import QtWebEngineWidgets