from PyQt4 import QtGui

from common_parametersform import Ui_ParameterWidget

class ParameterWidget(QtGui.QWidget,Ui_ParameterWidget):
    """ Widget that accepts input for parameters that all stimuli
     types have in common"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.tscale = 0.001 # display in ms

    def setScale(self, scale):
        self.tscale = scale
        # should also set labels!!!

    def intensityValue(self):
        return self.db_spnbx.value()

    def durationValue(self):
        return self.dur_spnbx.value()*self.tscale

    def risefallValue(self):
        return self.risefall_spnbx.value()*self.tscale

    def setField(self, **field):
        if 'intensity' in field:
            self.db_spnbx.setValue(field['intensity'])
        if 'duration' in field:
            self.dur_spnbx.setValue(field['duration']/self.tscale)
        if 'risefall' in field:
            self.risefall_spnbx.setValue(field['risefall']/self.tscale)

    def setFields(self, component):
        """Set all the input fields to the values in the provided component"""
        self.db_spnbx.setValue(component.intensity())
        self.dur_spnbx.setValue(component.duration()/self.tscale)
        self.risefall_spnbx.setValue(component.risefall()/self.tscale)

    def setDuration(self, duration):
        self.dur_spnbx.setValue(duration/self.tscale)