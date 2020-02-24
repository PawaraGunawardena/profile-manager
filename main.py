import time

from View import ProfileDataCollector
import Controller
from threading import Thread
import InternetConnection


def runGui():
    topelevel = ProfileDataCollector.vp_start_gui()

def runSynch():
    while True:
        try:
            if (InternetConnection.is_connected_to_network()):
                Controller.synachronize_sqlite_with_firebase()
            time.sleep(15)
        except:
            print("")
if __name__ == "__main__":
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



