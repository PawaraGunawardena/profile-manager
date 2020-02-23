import time

import ProfileDataCollector
import Controller
from threading import Thread
import InternetConnection
import tkinter
from tkinter import messagebox

def runGui():
    # while True:
    #
    #     topelevel = ProfileDataCollector.vp_start_gui()

    topelevel = ProfileDataCollector.vp_start_gui()

def runSynch():
    while True:
        if (InternetConnection.is_connected_to_network()):
            Controller.synachronize_sqlite_with_firebase()
        time.sleep(15)
        # print("T2")



if __name__ == "__main__":

    # if (not InternetConnection.is_connected_to_network()):
    #     print("No internet connectivity !")


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



