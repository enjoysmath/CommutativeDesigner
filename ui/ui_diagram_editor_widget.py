# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagram_editor_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiagramEditorWidget(object):
    def setupUi(self, DiagramEditorWidget):
        DiagramEditorWidget.setObjectName("DiagramEditorWidget")
        DiagramEditorWidget.resize(454, 239)
        self.gridLayout = QtWidgets.QGridLayout(DiagramEditorWidget)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(DiagramEditorWidget)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 0, 1, 2, 2)

        self.retranslateUi(DiagramEditorWidget)
        QtCore.QMetaObject.connectSlotsByName(DiagramEditorWidget)

    def retranslateUi(self, DiagramEditorWidget):
        _translate = QtCore.QCoreApplication.translate
        DiagramEditorWidget.setWindowTitle(_translate("DiagramEditorWidget", "Form"))
from PyQt5 import QtWebEngineWidgets
