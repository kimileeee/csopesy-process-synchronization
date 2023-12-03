import threading
import time
import random

class FittingRoom:
    def __init__(self, n):
        self.n_slots = n
        self.slots = threading.Semaphore(n)
        self.mutex = threading.Semaphore(1)
        self.turnstile = threading.Semaphore(1)
        self.current_color = None
        self.running_threads = []

    def enter_fitting_room(self, thread):
        self.running_threads.append(thread)
        while True:
            self.mutex.acquire()
            if self.current_color is None: # First thread to enter
                self.current_color = thread.color
                print(f"------------ {self.current_color.capitalize()} only ------------")
                self.slots.acquire()
                print(f"+ ENTR: Thread {thread.id} ({thread.color})")
                self.mutex.release()
                break

            elif self.current_color == thread.color:
                if self.slots._value > 0 and self.turnstile._value:
                    # if self.slots._value == 0:
                    #     print(f"------------ {self.current_color.capitalize()} only ------------")
                    self.slots.acquire()
                    print(f"+ ENTR: Thread {thread.id} ({thread.color})")
                    self.mutex.release()
                    break
                else:
                    if self.turnstile._value: # If turnstile is open, close it
                        self.turnstile.acquire()
            # else:
            #     print(f"----------Error: {color.capitalize()} thread {id} entering while {self.current_color.capitalize()} thread inside. Retrying...")
            self.mutex.release()
            time.sleep(1)

    def exit_fitting_room(self, thread):
        self.mutex.acquire()
        self.slots.release()
        self.running_threads.remove(thread)
        print(f"- EXIT: Thread {thread.id} ({thread.color})")
        if self.slots._value == self.n_slots:
            print("------- Empty fitting room -------")
            for t in self.running_threads:
                if t.color != self.current_color:
                    self.current_color = t.color
                    print(f"------------ {self.current_color.capitalize()} only ------------")
                    break
            self.turnstile.release()
            
        self.mutex.release()