import logging

from PyQt4 import QtGui

from spikeylab.stim.types.stimuli_classes import WhiteNoise, FMSweep
from spikeylab.stim.tceditor import TuningCurveEditor
from .calwidget_form import Ui_CalibrationWidget

class CalibrationWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CalibrationWidget,self).__init__(parent)
        self.ui = Ui_CalibrationWidget()
        self.ui.setupUi(self)
        self.ui.curve_widget.ui.ok_btn.hide()
        self.ui.curve_widget.ui.save_btn.hide()
        self.ui.curve_widget.ui.dur_spnbx.setEnabled(False)
        self.ui.curve_widget.ui.nreps_spnbx.hide()
        self.ui.curve_widget.ui.label_31.hide()
        self.duration_widgets = [self.ui.curve_widget.ui.dur_spnbx]

    def setCurveModel(self, model):
        """sets the StimulusModel for this calibration curve"""
        self.stim_model = model
        self.ui.curve_widget.setStimulusModel(model)

    def set_duration(self, dur):
        for w in self.duration_widgets:
            w.setValue(dur)

    def add_option(self, stim):
        # set the editor widgets for noise and sweep
        self.ui.cal_type_cmbbx.insertItem(0,stim.name)
        editor = stim.showEditor()
        # should probably make this less coupled
        dur_input = editor.duration_input_widget()
        self.duration_widgets.append(dur_input)
        dur_input.setEnabled(False)
        self.ui.caleditor_stack.insertWidget(0, editor)
        self.ui.cal_type_cmbbx.setCurrentIndex(0)

    def save_to_object(self):
        for i in range(self.ui.caleditor_stack.count()):
            try:
                self.ui.caleditor_stack.widget(i).saveToObject()
            except AttributeError:
                logger = logging.getLogger('main')
                logger.debug('index {} does not have method saveToObject'.format(i))

    def current_index(self):
        return self.ui.cal_type_cmbbx.currentIndex()

    def current_selection(self):
        return self.ui.cal_type_cmbbx.currentText()
        
    def is_tone_cal(self):
        return self.ui.cal_type_cmbbx.currentIndex() == self.ui.cal_type_cmbbx.count() -1

    def save_checked(self):
        return self.ui.savecal_ckbx.isChecked()