# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inference_rule_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InferenceRuleWidget(object):
    def setupUi(self, InferenceRuleWidget):
        InferenceRuleWidget.setObjectName("InferenceRuleWidget")
        InferenceRuleWidget.resize(435, 321)
        self.gridLayout = QtWidgets.QGridLayout(InferenceRuleWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(InferenceRuleWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(InferenceRuleWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(InferenceRuleWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.givensList = QtWidgets.QListWidget(InferenceRuleWidget)
        self.givensList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.givensList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.givensList.setFlow(QtWidgets.QListView.LeftToRight)
        self.givensList.setObjectName("givensList")
        self.gridLayout.addWidget(self.givensList, 1, 0, 1, 2)
        self.resultsList = QtWidgets.QListWidget(InferenceRuleWidget)
        self.resultsList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.resultsList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.resultsList.setFlow(QtWidgets.QListView.LeftToRight)
        self.resultsList.setObjectName("resultsList")
        self.gridLayout.addWidget(self.resultsList, 4, 0, 1, 2)

        self.retranslateUi(InferenceRuleWidget)
        QtCore.QMetaObject.connectSlotsByName(InferenceRuleWidget)

    def retranslateUi(self, InferenceRuleWidget):
        _translate = QtCore.QCoreApplication.translate
        InferenceRuleWidget.setWindowTitle(_translate("InferenceRuleWidget", "Form"))
        self.label_2.setText(_translate("InferenceRuleWidget", "Results:"))
        self.label.setText(_translate("InferenceRuleWidget", "Givens:"))
