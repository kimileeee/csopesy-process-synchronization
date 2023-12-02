import threading
import time
import random

class FittingRoom:
    BLUE = 'blue'
    GREEN = 'green'

    def __init__(self, n):
        self.n_slots = n
        self.slots = threading.Semaphore(n)
        self.mutex = threading.Semaphore(1)
        self.current_color = None

    def enter_fitting_room(self, id, color):

        while True:
            self.mutex.acquire()
            if self.current_color is None:
                self.current_color = color
                print(f"{color.capitalize()} only")
                if self.slots._value > 0:
                    self.slots.acquire()
                    print(f"Thread {id} ({color}) entered the fitting room.")
                    self.mutex.release()
                    break
                else:
                    # Fitting room is full, release the mutex and try again
                    print("----------Fitting room is full. Retrying...")
            elif self.current_color == color:
                if self.slots._value > 0:
                    self.slots.acquire()
                    print(f"Thread {id} ({color}) entered the fitting room.")
                    self.mutex.release()
                    break
                else:
                    # Fitting room is full, release the mutex and try again
                    print("----------Fitting room is full. Retrying...")
            else:
                # Another color is inside, release the mutex and try again
                print(f"----------Error: {color.capitalize()} thread {id} entering while {self.current_color.capitalize()} thread inside. Retrying...")
            self.mutex.release()
            time.sleep(1)

    def exit_fitting_room(self, id, color):
        self.mutex.acquire()
        # print(f"Thread {threading.current_thread().ident} ({color}) exited the fitting room.")
        self.slots.release()
        print(f"---------- EXIT: Thread {id}")
        if self.slots._value == self.n_slots:
            print("Empty fitting room.")
            self.current_color = None
        self.mutex.release()

def run_thread(id, color, fittingroom):
    fittingroom.enter_fitting_room(id, color)
    time.sleep(random.uniform(1, 5))
    fittingroom.exit_fitting_room(id, color)