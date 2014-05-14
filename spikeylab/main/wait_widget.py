from PyQt4 import QtCore, QtGui

class WaitWidget(QtGui.QLabel):
    def __init__(self, message= "Loading...", parent=None):
        QtGui.QLabel.__init__(self, parent)

        pts = 16
        self.setText(message)
        self.setWindowModality(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setPointSize(pts)
        self.setFont(font)
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Raised)
        self.setLineWidth(2)
        self.resize(len(message)*pts, pts+40)
