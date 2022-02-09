import time

class FPS():
    def __init__(self):
        self.counterLast = 0
        self.counter = 0
        self.start_time = time.time()

    def update(self):
        self.counter += 1
        self.checkUpdate()

    def checkUpdate(self):
        if (time.time() - self.start_time) > 1:
            self.counterLast = self.counter 
            self.counter = 0
            self.start_time = time.time()

    def show(self): return self.counterLast

