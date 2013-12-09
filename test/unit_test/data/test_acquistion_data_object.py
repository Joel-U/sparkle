import numpy as np
import os
from nose.tools import raises

from spikeylab.data.dataobjects import AcquisitionData, increment
from spikeylab.tools.exceptions import DataIndexError

tempfolder = os.path.join(os.path.abspath(os.path.dirname(__file__)), u"tmp")

def test_increment_index_by_1():
    dimensions = (2,3,4)
    data_shape = (1,)
    current_index = [0,0,1]

    current_index = increment(current_index, dimensions, data_shape)
    assert current_index == [0,0,2]

def test_increment_index_single_low_dimension():
    dimensions = (2,3,4)
    data_shape = (4,)
    current_index = [0,1,0]

    increment(current_index, dimensions, data_shape)
    assert current_index == [0,2,0]

def test_increment_index_double_low_dimension():
    dimensions = (2,3,4)
    data_shape = (1,4,)
    current_index = [0,0,0]

    current_index = increment(current_index, dimensions, data_shape)
    assert current_index == [0,1,0]

def test_increment_index_mid_dimension():
    dimensions = (2,3,4)
    data_shape = (2,4,)
    current_index = [0,0,0]

    current_index = increment(current_index, dimensions, data_shape)
    assert current_index == [0,2,0]

def test_increment_index_high_dimension():
    dimensions = (2,3,4)
    data_shape = (1,3,4,)
    current_index = [0,0,0]

    current_index = increment(current_index, dimensions, data_shape)
    assert current_index == [1,0,0]

@raises(DataIndexError)
def test_bad_data_shape():
    dimensions = (2,3,4)
    data_shape = (4,1)
    current_index = [0,0,0]

    current_index = increment(current_index, dimensions, data_shape)

class TestAcqusitionData():
    """
    Test creating, putting and getting to acquisition data structure
    """
    def test_finite_dataset_append(self):
        # such as for a tuning curve
        nsets = 3
        npoints = 10
        fakedata = np.ones((npoints,))

        fname = os.path.join(tempfolder, 'savetemp.hdf5')
        acq_data = AcquisitionData(fname)
            
        acq_data.init_data('fake', (nsets, npoints))
        for iset in range(nsets):
            acq_data.append('fake', fakedata*iset)

        np.testing.assert_array_equal(acq_data.get('fake', (1,)), fakedata*1)

        acq_data.close()

    def test_finite_dataset_append_double_dimension(self):
        # such as for a tuning curve
        nsets = 3
        npoints = 10
        fakedata = np.ones((1,npoints))

        fname = os.path.join(tempfolder, 'savetemp.hdf5')
        acq_data = AcquisitionData(fname)
            
        acq_data.init_data('fake', (nsets, npoints))
        for iset in range(nsets):
            acq_data.append('fake', fakedata*iset)

        np.testing.assert_array_equal(acq_data.get('fake', (2,)), np.squeeze(fakedata*2))

        acq_data.close()

    @raises(TypeError)
    def test_finite_dataset_append_error(self):
        # such as for a tuning curve
        nsets = 3
        npoints = 10
        fakedata = np.ones((npoints,))

        fname = os.path.join(tempfolder, 'savetemp.hdf5')
        acq_data = AcquisitionData(fname)
            
        try:
            acq_data.init_data('fake', (nsets, nsets))
            for iset in range(nsets):
                acq_data.append('fake', fakedata*iset)

            np.testing.assert_array_equal(acq_data.get('fake', (2,)), fakedata*2)
        finally:
            acq_data.close()

    def test_finite_dataset_insert(self):
        # such as for a tuning curve
        nsets = 3
        npoints = 10
        fakedata = np.ones((npoints,))

        fname = os.path.join(tempfolder, 'savetemp.hdf5')
        acq_data = AcquisitionData(fname)
            
        acq_data.init_data('fake', (nsets, npoints))
        for iset in range(nsets):
            acq_data.insert('fake', [iset], fakedata*iset)

        np.testing.assert_array_equal(acq_data.get('fake', (1,)), fakedata*1)

        acq_data.close()