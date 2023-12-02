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
        self.turnstile = threading.Semaphore(1)
        self.current_color = None

    def enter_fitting_room(self, id, color):
        # Thread will keep trying to enter the fitting room until it succeeds
        while True:
            self.mutex.acquire()
            if self.current_color is None: # First thread to enter
                self.current_color = color
                print(f"{self.current_color.capitalize()} only")
                self.slots.acquire()
                print(f"Thread {id} ({color}) entered the fitting room.")
                self.mutex.release()
                break

            elif self.current_color == color:
                if self.slots._value > 0 and self.turnstile._value:
                    self.slots.acquire()
                    print(f"Thread {id} ({color}) entered the fitting room.")
                    self.mutex.release()
                    break
                else:
                    if self.turnstile._value: # If turnstile is open, close it
                        self.turnstile.acquire()
            # else:
            #     print(f"----------Error: {color.capitalize()} thread {id} entering while {self.current_color.capitalize()} thread inside. Retrying...")
            self.mutex.release()
            time.sleep(1)


    def exit_fitting_room(self, id, color):
        self.mutex.acquire()
        self.slots.release()
        print(f"----------EXIT: Thread {id}")
        if self.slots._value == self.n_slots:
            print("Empty fitting room.")
            # self.current_color = None
            self.turnstile.release()
            self.current_color = self.GREEN if self.current_color == self.BLUE else self.BLUE
            
        self.mutex.release()


def run_thread(id, color, fittingroom):
    fittingroom.enter_fitting_room(id, color)
    time.sleep(random.uniform(1, 5))
    fittingroom.exit_fitting_room(id, color)