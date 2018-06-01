from queue import Queue

class Printer:
    def __init__(self, ppm):
        self.pagerate =ppm
        self.currentTask =None
        self.timeRemaining =0
    

    def tick(self):
        