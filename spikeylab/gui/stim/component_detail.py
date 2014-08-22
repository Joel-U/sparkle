from PyQt4 import QtGui

class ComponentsDetailWidget(QtGui.QWidget):
    """class that presents the stimulus doc in a clear and useful way"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)

        self.lyt = QtGui.QVBoxLayout()
        self.setLayout(self.lyt)

        # keeps track of which attributes to display
        self.displayTable = {}
        self.defaultAttributes = ['intensity', 'risefall']
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

    def setDisplayTable(self, table):
        self.displayTable = table

    def setDefaultAttributes(self, defaults):
        self.defaultAttributes = defaults

    def setDoc(self, docs):
        # sort stim by start time
        docs = sorted(docs, key=lambda k: k['start_s'])

        for doc in docs:
            stim_type = doc['stim_type']
            if not stim_type in self.displayTable:
                continue
            if not stim_type in self.displayTable[stim_type]:
                continue
            display_attributes = self.displayTable.get(stim_type, self.defaultAttributes)
            
            self.lyt.addWidget(ComponentDetailFrame(doc, display_attributes))

    def clearDoc(self):
        clearLayout(self.lyt)

class ComponentDetailFrame(QtGui.QFrame):
    def __init__(self, comp_doc, displayAttributes, parent=None):
        QtGui.QFrame.__init__(self)

        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Raised)
        font = QtGui.QFont()
        font.setPointSize(14)

        glay = QtGui.QGridLayout()
        stim_type = comp_doc['stim_type']

        # always at least include stimulus type
        title = QtGui.QLabel(stim_type)
        title.setFont(font)
        glay.addWidget(title,0,0)
        # get any other attributes to display, or defaults if not specified
        for i, attr in enumerate(displayAttributes):
            if attr == stim_type:
                continue # already got it
            val = comp_doc[attr]
            # add to UI
            glay.addWidget(QtGui.QLabel(attr),i+1,0)
            glay.addWidget(QtGui.QLabel(str(val)),i+1,1)
            
        self.setLayout(glay)

class ComponentsDetailSelector(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

    def setComponents(self, components):
        layout = self.layout()
        for comp in components:
            attrWidget = ComponentAttributerChecker(comp)
            layout.addWidget(attrWidget)

    def setCheckedDetails(self, checked):
        layout = self.layout()
        for i in range(layout.count()):
            w = layout.itemAt(i).widget()
            if w.stimType in checked:
                w.setChecked(checked[w.stimType])

    def getCheckedDetails(self):
        attrs = {}
        layout = self.layout()
        for i in range(layout.count()):
            w = layout.itemAt(i).widget()
            attrs[w.stimType] = w.getChecked()
        return attrs

class ComponentAttributerChecker(QtGui.QFrame):
    def __init__(self, compAttributes, parent=None):
        QtGui.QFrame.__init__(self)

        self.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        layout = QtGui.QGridLayout()

        font = QtGui.QFont()
        font.setBold(True)
        stimType = compAttributes.pop('stim_type')
        title = QtGui.QCheckBox(stimType)
        title.setFont(font)
        layout.addWidget(title,0,0)

        for i, key in enumerate(compAttributes):
            layout.addWidget(QtGui.QCheckBox(key),i+1,0)

        self.setLayout(layout)
        self.stimType = stimType


    def setChecked(self, tocheck):
        layout = self.layout()
        for i in range(layout.count()):
            w = layout.itemAt(i).widget()
            if w.text() in tocheck:
                w.setChecked(True)

    def getChecked(self):
        attrs = []
        layout = self.layout()
        for i in range(layout.count()):
            w = layout.itemAt(i).widget()
            if w.isChecked():
                attrs.append(str(w.text()))
        return attrs

def clearLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clearLayout(item.layout())