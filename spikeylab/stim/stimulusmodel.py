import numpy as np

from spikeylab.stim.auto_parameter_modelview import AutoParameterModel

from PyQt4 import QtGui, QtCore

# COLORTABLE=cm.get_cmap('jet')
COLORTABLE = []
for i in range(16): COLORTABLE.append(QtGui.qRgb(i/4,i,i/2))

class StimulusModel(QtCore.QAbstractItemModel):
    """
    Model to represent any stimulus the system will present. 
    Holds all relevant parameters
    """
    def __init__(self, parent=None):
        QtCore.QAbstractItemModel.__init__(self, parent)
        self.nreps = 0
        self.samplerate = 375000
        # 2D array of simulus components track number x component number
        self.segments = [[]]
        # add an empty place to place components into new track
        self.auto_params = AutoParameterModel()

        # reference for what voltage == what intensity
        self.calv = 0.1
        self.caldb = 100

    def setSamplerate(self, fs):
        self.samplerate = fs

    def setAutoParams(self, params):
        self.auto_params = params

    def autoParams(self):
        return self.auto_params

    def headerData(self, section, orientation, role):
        return ''

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.segments)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            print 'querying column count by parent'
            wholerow = parent.internalPointer()
            return len(wholerow)
        else:
            column_lengths = [len(x) for x in self.segments]
            return max(column_lengths)

    def columnCountForRow(self, row):
        return len(self.segments[row])

    def data(self, index, role):
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole:
            component = self.segments[index.row()][index.column()]
            return component.__class__.__name__
        elif role == QtCore.Qt.UserRole:  #return the whole python object
            if len(self.segments[index.row()]) > index.column():
                component = self.segments[index.row()][index.column()]
            else:
                component = None
            return component
        elif role == QtCore.Qt.SizeHintRole:
            component = self.segments[index.row()][index.column()]
            return component.duration() #* PIXELS_PER_MS * 1000

    def printStimulus(self):
        """This is for purposes of documenting what was presented"""


    def index(self, row, col, parent=QtCore.QModelIndex()):
        # need to convert row, col to correct element, however still have heirarchy?
        if parent.isValid():
            print 'valid parent', parent.row(), parent.col()
            prow = self.segments.index(parent.internalPointer())
            return self.createIndex(prow, row, self.segments[prow][row])
        else:
            if row < len(self.segments) and col < len(self.segments[row]):
                return self.createIndex(row, col, self.segments[row][col])
            else:
                return QtCore.QModelIndex()

    def parentForRow(self, row):
        # get the whole row
        return self.createIndex(row, -1, self.segments[row])

    def parent(self, index):
        if index.column() == -1:
            return QtCore.QModelIndex()
        else:
            return self.createIndex(index.row(), -1, self.segments[index.row()])

    def insertComponent(self, comp, rowcol=(0,0)):
        parent = self.parentForRow(rowcol[0])
        # convert to index or done already?
        self.beginInsertRows(parent, rowcol[1], rowcol[1])
        parent.internalPointer().insert(rowcol[1], comp)
        self.endInsertRows()

        if len(self.segments[-1]) > 0:
            self.beginInsertRows(QtCore.QModelIndex(), len(self.segments), len(self.segments))
            self.segments.append([])
            self.endInsertRows()

        # special case, where component is a wav file:
        # it will set the master samplerate to match its own
        if comp.__class__.__name__ == 'Vocalization':
            self.samplerate = comp.samplerate()

    def removeComponent(self, rowcol):
        parent = self.parentForRow(rowcol[0])

        self.beginRemoveRows(parent, rowcol[1], rowcol[1])
        parent.internalPointer().pop(rowcol[1])
        self.endRemoveRows()

        if len(self.segments[-2]) == 0:
            self.beginRemoveRows(QtCore.QModelIndex(), len(self.segments)-1, len(self.segments)-1)
            self.segments.pop(len(self.segments)-1)
            self.endRemoveRows()

    def clearComponents(self):
        self.segments = [[]]

    def indexByComponent(self, component):
        """return a QModelIndex for the given component, or None if
        it is not in the model"""
        for row, rowcontents in enumerate(self.segments):
            if component in rowcontents:
                column = rowcontents.index(component)
                return self.index(row, column)

    def setData(self, index, value):
        # item must already exist at provided index
        self.segments[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable| QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


    def traceCount()(self):
        params = self.auto_params.allData()
        steps = []
        ntraces = 1
        for p in params:
            steps.append(np.arange(p['start'], p['stop'], p['delta']))
            ntraces = ntraces*len(steps[-1])
        return ntraces

    def expandedStim(self):
        """
        Apply the autoparameters to this stimulus and return a list of
        the resulting stimuli
        """
        stim_list = self.expandFucntion(self.signal)
        return stim_list

    def expandFucntion(self, func):
        # initilize array to hold all varied parameters
        params = self.auto_params.allData()
        steps = []
        ntraces = 1
        for p in params:
            steps.append(np.arange(p['start'], p['stop'], p['delta']))
            ntraces = ntraces*len(steps[-1])

        varylist = [[None for x in range(len(params))] for y in range(ntraces)]
        x = 1
        for iset, step_set in enumerate(steps):
            for itrace in range(ntraces):
                idx = (itrace / x) % len(step_set)
                varylist[itrace][iset] = step_set[idx]
            x = x*len(step_set)
            
        # now create the stimuli according to steps
        # go through list of modifing parameters, update this stimulus,
        # and then save current state to list
        stim_list = []
        for itrace in range(ntraces):
            for ip, param in enumerate(params):
                comp_inds = self.auto_params.selection(param)
                for index in comp_inds:
                    component = self.data(index, QtCore.Qt.UserRole)
                    component.set(param['parameter'], varylist[itrace][ip])
            # copy of current stim state, or go ahead and turn it into a signal?
            # so then would I want to formulate some doc here as well?
            stim_list.append(func())

        # now reset the components to start value
        for ip, param in enumerate(params):
            comp_inds = self.auto_params.selection(param)
            for index in comp_inds:
                component = self.data(index, QtCore.Qt.UserRole)
                component.set(param['parameter'], varylist[0][ip])

        return stim_list

    def expandedDoc(self):
        """
        JSON/YAML/XML representation of exactly what was presented
        """
        doc_list = self.expandFucntion(self.doc)
        return doc_list

    def templateDoc(self):
        """
        JSON/YAML/XML template to recreate this stimulus in another session
        """

    def signal(self):
        """Return the current stimulus in signal representation"""
        track_signals = []
        max_db = max([comp.intensity() for t in self.segments for comp in t])
        caldb = 100
        atten = caldb - max_db
        for track in self.segments:
            # nsamples = sum([comp.duration() for comp in track])*self.samplerate
            # track_signal = np.zeros((nsamples,))
            track_list = []
            for component in track:
                track_list.append(component.signal(self.samplerate, atten))
            if len(track_list) > 0:   
                track_signals.append(np.hstack(track_list))

        # track_signals = sorted(track_signals, key=len, reverse=True)
        full_len = len(max(track_signals, key=len))
        total_signal = np.zeros((full_len,))
        for track in track_signals:
            total_signal[0:len(track)] += track

        return total_signal, atten

    def doc(self):
        doc_list = []
        for track in self.segments:
            start_time = 0
            for component in track:
                info = component.stateDict()
                info['stim_type'] = component.name
                info['start_s'] = start_time
                start_time += info['duration']
                doc_list.append(info)

        return {'samplerate_da':self.samplerate, 'reps': self.nreps, 
                'calv': self.calv, 'caldb':self.caldb, 'components': doc_list}