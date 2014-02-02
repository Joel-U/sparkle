# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calibration_dlg.ui'
#
# Created: Sat Feb 01 08:11:08 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CalibrationDialog(object):
    def setupUi(self, CalibrationDialog):
        CalibrationDialog.setObjectName(_fromUtf8("CalibrationDialog"))
        CalibrationDialog.resize(426, 231)
        self.verticalLayout_2 = QtGui.QVBoxLayout(CalibrationDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(CalibrationDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.none_radio = QtGui.QRadioButton(self.groupBox)
        self.none_radio.setChecked(True)
        self.none_radio.setObjectName(_fromUtf8("none_radio"))
        self.verticalLayout.addWidget(self.none_radio)
        self.calfile_radio = QtGui.QRadioButton(self.groupBox)
        self.calfile_radio.setObjectName(_fromUtf8("calfile_radio"))
        self.verticalLayout.addWidget(self.calfile_radio)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.calfile_lnedt = QtGui.QLineEdit(self.groupBox)
        self.calfile_lnedt.setEnabled(False)
        self.calfile_lnedt.setObjectName(_fromUtf8("calfile_lnedt"))
        self.horizontalLayout.addWidget(self.calfile_lnedt)
        self.browse_btn = QtGui.QPushButton(self.groupBox)
        self.browse_btn.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_btn.sizePolicy().hasHeightForWidth())
        self.browse_btn.setSizePolicy(sizePolicy)
        self.browse_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.browse_btn.setObjectName(_fromUtf8("browse_btn"))
        self.horizontalLayout.addWidget(self.browse_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.calv_spnbx = QtGui.QDoubleSpinBox(CalibrationDialog)
        self.calv_spnbx.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.calv_spnbx.setMaximum(1.0)
        self.calv_spnbx.setObjectName(_fromUtf8("calv_spnbx"))
        self.gridLayout.addWidget(self.calv_spnbx, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(CalibrationDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.caldb_spnbx = QtGui.QSpinBox(CalibrationDialog)
        self.caldb_spnbx.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.caldb_spnbx.setMaximum(110)
        self.caldb_spnbx.setObjectName(_fromUtf8("caldb_spnbx"))
        self.gridLayout.addWidget(self.caldb_spnbx, 0, 1, 1, 1)
        self.label = QtGui.QLabel(CalibrationDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(CalibrationDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.calf_spnbx = SmartSpinBox(CalibrationDialog)
        self.calf_spnbx.setMaximum(200000.0)
        self.calf_spnbx.setObjectName(_fromUtf8("calf_spnbx"))
        self.gridLayout.addWidget(self.calf_spnbx, 2, 1, 1, 1)
        self.funit_lbl = QtGui.QLabel(CalibrationDialog)
        self.funit_lbl.setObjectName(_fromUtf8("funit_lbl"))
        self.gridLayout.addWidget(self.funit_lbl, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(CalibrationDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_6 = QtGui.QLabel(CalibrationDialog)
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(CalibrationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(CalibrationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CalibrationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CalibrationDialog.reject)
        QtCore.QObject.connect(self.none_radio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.calfile_lnedt.setDisabled)
        QtCore.QObject.connect(self.none_radio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.browse_btn.setDisabled)
        QtCore.QObject.connect(self.browse_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), CalibrationDialog.browseFiles)
        QtCore.QMetaObject.connectSlotsByName(CalibrationDialog)

    def retranslateUi(self, CalibrationDialog):
        CalibrationDialog.setWindowTitle(_translate("CalibrationDialog", "Dialog", None))
        self.groupBox.setTitle(_translate("CalibrationDialog", "Calibration file", None))
        self.none_radio.setText(_translate("CalibrationDialog", "None", None))
        self.calfile_radio.setText(_translate("CalibrationDialog", "Use saved calibration", None))
        self.browse_btn.setText(_translate("CalibrationDialog", "...", None))
        self.label_2.setText(_translate("CalibrationDialog", "Reference voltage", None))
        self.label.setText(_translate("CalibrationDialog", "Reference dB", None))
        self.label_3.setText(_translate("CalibrationDialog", "calibration frequency", None))
        self.funit_lbl.setText(_translate("CalibrationDialog", "kHz", None))
        self.label_5.setText(_translate("CalibrationDialog", "V", None))
        self.label_6.setText(_translate("CalibrationDialog", "dB SPL", None))

from spikeylab.stim.smart_spinbox import SmartSpinBox