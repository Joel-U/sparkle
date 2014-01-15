import sip
sip.setapi('QVariant', 2)
sip.setapi('QString', 2)

import sys
import time

from PyQt4.QtGui import QApplication
import numpy as np

from spikeylab.plotting.protocoldisplay import ProtocolDisplay


PAUSE = 3

class TestProtocolDisplay():

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.t = np.arange(200)

    def data_func(self, f):
        return 2*np.sin(2*np.pi*f*self.t/len(self.t))

    def test_display(self):
        display = ProtocolDisplay()
        display.show()

        display.set_nreps(5)

        # generate dummy 2D data
        xy_range = (-200, 200)
        x = np.linspace(xy_range[0], xy_range[1], 100)
        y = np.linspace(xy_range[0], xy_range[1], 100)
        X,Y = np.meshgrid(x, y)
        Z = np.sin(X)*np.arctan2(Y,X)

        display.update_spec(Z, xaxis=x, yaxis=y)

        data = self.data_func(3)
        nbins = 50
        bin_centers = np.linspace(0, self.t[-1], nbins)
        points = np.ones(nbins)

        display.update_signal(self.t, data)
        display.update_spiketrace(self.t, data)
        display.update_fft(self.t, data)
        display.add_raster_points(bin_centers, points)
        display.add_raster_points(bin_centers, points*2)

        display.set_xlimits((self.t[0], self.t[-1]))
        display.set_tscale(0.001)
        display.set_fscale(1000)

        QApplication.processEvents()

        display.clear_raster()

        time.sleep(PAUSE)