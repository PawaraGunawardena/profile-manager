import time

import ProfileDataCollector
import Controller
from threading import Thread
import InternetConnection


def runGui():
    while True:
        topelevel = ProfileDataCollector.vp_start_gui()
        # topelevel.update_treeview()
        print("T1")

# def runGui():
#
#     topelevel = ProfileDataCollector.vp_start_gui()
#     topelevel.update_treeview()
#     print("T1")

def runSynch():
    while True:
        if (InternetConnection.is_connected_to_network()):
            Controller.synachronize_sqlite_with_firebase()
        # time.sleep(1)
        print("T2")



if __name__ == "__main__":
    # ProfileDataCollector.vp_start_gui()
    t1 = Thread(target = runGui)
    t2 = Thread(target = runSynch)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    while True:
        pass



