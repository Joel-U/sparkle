# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tuning_curve.ui'
#
# Created: Wed Feb 26 16:48:33 2014
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

class Ui_TuningCurveEditor(object):
    def setupUi(self, TuningCurveEditor):
        TuningCurveEditor.setObjectName(_fromUtf8("TuningCurveEditor"))
        TuningCurveEditor.resize(599, 285)
        self.verticalLayout = QtGui.QVBoxLayout(TuningCurveEditor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.db_stop_spnbx = QtGui.QSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_stop_spnbx.setFont(font)
        self.db_stop_spnbx.setMaximum(120)
        self.db_stop_spnbx.setProperty("value", 110)
        self.db_stop_spnbx.setObjectName(_fromUtf8("db_stop_spnbx"))
        self.gridLayout_2.addWidget(self.db_stop_spnbx, 2, 2, 1, 1)
        self.freq_stop_spnbx = QtGui.QSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freq_stop_spnbx.setFont(font)
        self.freq_stop_spnbx.setMaximum(200)
        self.freq_stop_spnbx.setProperty("value", 150)
        self.freq_stop_spnbx.setObjectName(_fromUtf8("freq_stop_spnbx"))
        self.gridLayout_2.addWidget(self.freq_stop_spnbx, 1, 2, 1, 1)
        self.label_21 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 2, 4, 1, 1)
        self.funit_lbl_0 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funit_lbl_0.sizePolicy().hasHeightForWidth())
        self.funit_lbl_0.setSizePolicy(sizePolicy)
        self.funit_lbl_0.setObjectName(_fromUtf8("funit_lbl_0"))
        self.gridLayout_2.addWidget(self.funit_lbl_0, 1, 4, 1, 1)
        self.freq_start_spnbx = QtGui.QSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freq_start_spnbx.setFont(font)
        self.freq_start_spnbx.setMaximum(200)
        self.freq_start_spnbx.setSingleStep(5)
        self.freq_start_spnbx.setProperty("value", 5)
        self.freq_start_spnbx.setObjectName(_fromUtf8("freq_start_spnbx"))
        self.gridLayout_2.addWidget(self.freq_start_spnbx, 1, 1, 1, 1)
        self.db_start_spnbx = QtGui.QSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_start_spnbx.setFont(font)
        self.db_start_spnbx.setMaximum(150)
        self.db_start_spnbx.setSingleStep(5)
        self.db_start_spnbx.setProperty("value", 0)
        self.db_start_spnbx.setObjectName(_fromUtf8("db_start_spnbx"))
        self.gridLayout_2.addWidget(self.db_start_spnbx, 2, 1, 1, 1)
        self.label_25 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_2.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QtGui.QLabel(TuningCurveEditor)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_2.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_27 = QtGui.QLabel(TuningCurveEditor)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_28 = QtGui.QLabel(TuningCurveEditor)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_2.addWidget(self.label_28, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.db_nsteps_lbl = QtGui.QLabel(TuningCurveEditor)
        self.db_nsteps_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_nsteps_lbl.setObjectName(_fromUtf8("db_nsteps_lbl"))
        self.gridLayout_2.addWidget(self.db_nsteps_lbl, 2, 5, 1, 1)
        self.label_3 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 5, 1, 1)
        self.freq_nsteps_lbl = QtGui.QLabel(TuningCurveEditor)
        self.freq_nsteps_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.freq_nsteps_lbl.setObjectName(_fromUtf8("freq_nsteps_lbl"))
        self.gridLayout_2.addWidget(self.freq_nsteps_lbl, 1, 5, 1, 1)
        self.db_step_spnbx = SmartSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_step_spnbx.setFont(font)
        self.db_step_spnbx.setObjectName(_fromUtf8("db_step_spnbx"))
        self.gridLayout_2.addWidget(self.db_step_spnbx, 2, 3, 1, 1)
        self.freq_step_spnbx = SmartSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freq_step_spnbx.setFont(font)
        self.freq_step_spnbx.setObjectName(_fromUtf8("freq_step_spnbx"))
        self.gridLayout_2.addWidget(self.freq_step_spnbx, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_14 = QtGui.QLabel(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 3, 1, 1)
        self.label_22 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)
        self.tunit_lbl_4 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tunit_lbl_4.sizePolicy().hasHeightForWidth())
        self.tunit_lbl_4.setSizePolicy(sizePolicy)
        self.tunit_lbl_4.setObjectName(_fromUtf8("tunit_lbl_4"))
        self.gridLayout_3.addWidget(self.tunit_lbl_4, 0, 2, 1, 1)
        self.tunit_lbl_3 = QtGui.QLabel(TuningCurveEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tunit_lbl_3.sizePolicy().hasHeightForWidth())
        self.tunit_lbl_3.setSizePolicy(sizePolicy)
        self.tunit_lbl_3.setObjectName(_fromUtf8("tunit_lbl_3"))
        self.gridLayout_3.addWidget(self.tunit_lbl_3, 0, 5, 1, 1)
        self.nreps_spnbx = QtGui.QSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nreps_spnbx.setFont(font)
        self.nreps_spnbx.setMinimum(1)
        self.nreps_spnbx.setMaximum(100)
        self.nreps_spnbx.setProperty("value", 5)
        self.nreps_spnbx.setObjectName(_fromUtf8("nreps_spnbx"))
        self.gridLayout_3.addWidget(self.nreps_spnbx, 1, 4, 1, 1)
        self.label_31 = QtGui.QLabel(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_3.addWidget(self.label_31, 1, 3, 1, 1)
        self.dur_spnbx = SmartSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dur_spnbx.setFont(font)
        self.dur_spnbx.setMaximum(1000.0)
        self.dur_spnbx.setObjectName(_fromUtf8("dur_spnbx"))
        self.gridLayout_3.addWidget(self.dur_spnbx, 0, 1, 1, 1)
        self.risefall_spnbx = SmartSpinBox(TuningCurveEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risefall_spnbx.setFont(font)
        self.risefall_spnbx.setObjectName(_fromUtf8("risefall_spnbx"))
        self.gridLayout_3.addWidget(self.risefall_spnbx, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.save_btn = QtGui.QPushButton(TuningCurveEditor)
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.horizontalLayout.addWidget(self.save_btn)
        self.ok_btn = QtGui.QPushButton(TuningCurveEditor)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.horizontalLayout.addWidget(self.ok_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TuningCurveEditor)
        QtCore.QObject.connect(self.ok_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TuningCurveEditor.close)
        QtCore.QObject.connect(self.nreps_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.setStimReps)
        QtCore.QObject.connect(self.freq_start_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.submit)
        QtCore.QObject.connect(self.db_start_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.submit)
        QtCore.QObject.connect(self.freq_stop_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.submit)
        QtCore.QObject.connect(self.db_stop_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.submit)
        QtCore.QObject.connect(self.dur_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.setStimDuration)
        QtCore.QObject.connect(self.risefall_spnbx, QtCore.SIGNAL(_fromUtf8("editingFinished()")), TuningCurveEditor.setStimRisefall)
        QtCore.QObject.connect(self.save_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), TuningCurveEditor.saveStimulus)
        QtCore.QMetaObject.connectSlotsByName(TuningCurveEditor)

    def retranslateUi(self, TuningCurveEditor):
        TuningCurveEditor.setWindowTitle(_translate("TuningCurveEditor", "Form", None))
        self.label_21.setText(_translate("TuningCurveEditor", "dB SPL", None))
        self.funit_lbl_0.setText(_translate("TuningCurveEditor", "kHz", None))
        self.label_25.setText(_translate("TuningCurveEditor", "Frequency", None))
        self.label_26.setText(_translate("TuningCurveEditor", "Start", None))
        self.label_18.setText(_translate("TuningCurveEditor", "Intensity", None))
        self.label_27.setText(_translate("TuningCurveEditor", "Stop", None))
        self.label_28.setText(_translate("TuningCurveEditor", "Step", None))
        self.db_nsteps_lbl.setText(_translate("TuningCurveEditor", "0", None))
        self.label_3.setText(_translate("TuningCurveEditor", "No. steps", None))
        self.freq_nsteps_lbl.setText(_translate("TuningCurveEditor", "0", None))
        self.label_14.setText(_translate("TuningCurveEditor", "Rise fall time", None))
        self.label_22.setText(_translate("TuningCurveEditor", "Duration", None))
        self.tunit_lbl_4.setText(_translate("TuningCurveEditor", "ms", None))
        self.tunit_lbl_3.setText(_translate("TuningCurveEditor", "ms", None))
        self.label_31.setText(_translate("TuningCurveEditor", "Reps", None))
        self.save_btn.setText(_translate("TuningCurveEditor", "Save As...", None))
        self.ok_btn.setText(_translate("TuningCurveEditor", "Ok", None))

from spikeylab.stim.smart_spinbox import SmartSpinBox
