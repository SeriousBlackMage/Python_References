import threading
import time

class myThread(threading.Thread):
    def __init__(self, Id, name):
        threading.Thread.__init__(self)
        self.Id = Id
        self.name = name

    def run(self):
        print("starte", self.Id)
        time.sleep()
