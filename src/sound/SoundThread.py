import threading
import src.__main__ as main


class SoundThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        main.start()
