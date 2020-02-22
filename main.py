import time

import ProfileDataCollector
import Controller
from threading import Thread
import InternetConnection

def runGui():
    while True:
        ProfileDataCollector.vp_start_gui()

def runSynch():
    while True:
        if (InternetConnection.is_connected_to_network()):
            Controller.synachronize_sqlite_with_firebase()
        time.sleep(1000)

if __name__ == "__main__":
    t1 = Thread(target = runGui)
    t2 = Thread(target = runSynch)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()

    while True:
        pass



