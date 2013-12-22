from PyQt4 import QtGui

class AbstractParameterWidget(QtGui.QWidget):
    scales = [0.001, 1000] # time, frequency scaling factors
    funit_labels = []
    tunit_labels = []
    _component = None
    
    def setFScale(self, fscale):
        """
        Updates the frequency unit labels, and stores unit to
        to convert input before returning values in correct scale.
        """
        self.scales[1] = fscale
        if fscale == 1000:
            for lbl in self.funit_labels:
                lbl.setText('kHz')
        elif fscale == 1:
            for lbl in self.funit_labels:
                lbl.setText('Hz')
        else:
            raise Exception(u"Invalid frequency scale:"+str(self.fscale))

    def setTScale(self, tscale):
        """
        Updates the time unit labels, and stores unit to
        to convert input before returning values in correct scale.
        """
        self.scales[0] = tscale
        if tscale == 0.001:
            for lbl in self.tunit_labels:
                lbl.setText('ms')
        elif tscale == 1:
            for lbl in self.tunit_labels:
                lbl.setText('s')
        else:
            raise Exception(u"Invalid time scale:"+str(self.tscale))

    def name(self):
        return self._component.name

    def setComponent(self, component):
        raise NotImplementedError

    def saveToObject(self):
        raise NotImplementedError

