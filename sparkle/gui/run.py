import getpass
import logging
import time
import traceback
import sys

import os

from sparkle.QtWrapper import QtCore, QtGui
from sparkle.gui.dialogs import SavingDialog
from sparkle.gui.main_control import MainWindow
from sparkle.resources import icons
from sparkle.tools.systools import get_drives, get_free_mb

try:
    import PyDAQmx
    REVIEWMODE = False
except:
    REVIEWMODE = True

def log_uncaught(*exc_info):
    logger = logging.getLogger('main')
    logger.error("Uncaught exception: ", exc_info=exc_info)

def enable_review_mode():
    # Checks if there is an environment variable named SPARKLE_DEVELOP.
    # If SPARKLE_DEVELOP exists and is equal to true, enable_review_mode() will
    # return false.
    # Is SPARKLE_DEVELOP exists and is not equal to true, enable_review_mode()
    # will return true.
    # If SPARKLE_DEVELOP does not exist enable_review_mode() will return True.
    sparkle_develop = os.environ.get('SPARKLE_DEVELOP')
    if sparkle_develop is None:
        sparkle_develop = 'False'
    if sparkle_develop.upper() != 'TRUE':
        return True
    else:
        print 'Entering Developer Mode'
        return False

def main():
    global REVIEWMODE
    if REVIEWMODE:
        REVIEWMODE = enable_review_mode()

    # this is the entry point for the whole application
    logger = logging.getLogger('main')
    logger.info("{} Program Started {}, user: {} {}".format('*'*8, time.strftime("%d-%m-%Y"), getpass.getuser(), '*'*8))
    
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(icons.windowicon())
    sys.excepthook = log_uncaught
    # check free drive space, issue warning if low
    drives = get_drives()
    low_space = []
    plenty_space = []
    try:
        for drive in drives:
            space = get_free_mb(drive)
            if space < 1024:
                low_space.append((drive, space))
            else:
                plenty_space.append((drive, space))
        if len(low_space) > 0:
            if len(plenty_space) > 0:
                msg = "Warning: At least one Hard disk has low free space:\n\nDrives with low space:\n"
                for drive in low_space:
                    msg = msg + "{} : {} MB\n".format(drive[0], drive[1])
                msg = msg + "\nDrives with more space:\n"
                for drive in plenty_space:
                    msg = msg + "{} : {} MB\n".format(drive[0], drive[1])
                msg = msg + "\nYou are advised to only save data to a drive with enough available space"
                QtGui.QMessageBox.warning(None, "Drive space low", msg)
            else:
                msg = "Warning: All Hard disks have low free space:\n\n"
                for drive in low_space:
                    msg = msg + "{} : {} MB\n".format(drive[0], drive[1])
                msg = msg + "\nIt is recommended that you free up space on a drive before conducting experiments"
                QtGui.QMessageBox.warning(None, "Drive space low", msg)

        dlg = SavingDialog()
        if dlg.exec_():
            fname, fmode = dlg.getfile()
            main_window = MainWindow("controlinputs.json", datafile=fname, filemode=fmode, hidetabs=REVIEWMODE)
            app.setActiveWindow(main_window)
            main_window.show()
            status = app.exec_()
        else:
            status = 0
            print 'canceled'
        dlg.deleteLater()
    except Exception, e:
        msg = str(e) + '\nTraceback:\n\n'
        tb = traceback.format_tb(sys.exc_info()[2])
        for line in tb:
            msg += line
        QtGui.QMessageBox.critical(None, "Unexpected Error", msg)
        status = 0
        raise

    logger.info("== Program finished with exit code {} ==".format(status))
    sys.exit(status)

if __name__ == "__main__":
    main()
