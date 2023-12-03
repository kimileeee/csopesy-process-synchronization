import threading
import time
import random

class CustomThread(threading.Thread):
    def __init__(self, id, color, fitting_room, priority=0):
        super().__init__()
        self.id = id
        self.fitting_room = fitting_room
        self.color = color
        self.priority = priority

    def run(self):
        self.fitting_room.enter_fitting_room(self)
        self.fit_clothes()
        self.fitting_room.exit_fitting_room(self)

    def fit_clothes(self):
        time.sleep(random.uniform(1, 5))


class BlueThread(CustomThread):
    COLOR = "Blue"

    def __init__(self, id, fitting_room):
        super().__init__(id, self.COLOR, fitting_room)


class GreenThread(CustomThread):
    COLOR = "Green"

    def __init__(self, id, fitting_room):
        super().__init__(id, self.COLOR, fitting_room)