import threading
import time
import random

class FittingRoom:
    def __init__(self, n):
        self.n = n
        self.mutex = threading.Lock()
        self.blue_turnstile = threading.Condition(self.mutex)
        self.green_turnstile = threading.Condition(self.mutex)
        self.blue_count = 0
        self.green_count = 0

    def enter_room(self, color):
        with self.mutex:
            if color == 'blue':
                self.blue_count += 1
                if self.blue_count == 1:
                    print("Blue only.")
                else:
                    self.blue_turnstile.wait()
            elif color == 'green':
                self.green_count += 1
                if self.green_count == 1:
                    print("Green only.")
                else:
                    self.green_turnstile.wait()

            # Thread enters the fitting room
            print(f"Thread {threading.current_thread().ident} ({color}) entered.")

    def exit_room(self, color):
        with self.mutex:
            # Thread exits the fitting room
            print(f"Thread {threading.current_thread().ident} ({color}) exited.")

            if color == 'blue':
                self.blue_count -= 1
                if self.blue_count == 0:
                    print("Empty fitting room.")
                    self.green_turnstile.notify_all()
                else:
                    self.blue_turnstile.notify()
            elif color == 'green':
                self.green_count -= 1
                if self.green_count == 0:
                    print("Empty fitting room.")
                    self.blue_turnstile.notify_all()
                else:
                    self.green_turnstile.notify()

def simulate_fitting_room(n, b, g):
    fitting_room = FittingRoom(n)
    threads = []

    def thread_function(color):
        fitting_room.enter_room(color)
        # Simulate some work inside the fitting room
        time.sleep(random.uniform(1, 5))
        fitting_room.exit_room(color)

    for _ in range(b):
        thread = threading.Thread(target=thread_function, args=('blue',))
        threads.append(thread)

    for _ in range(g):
        thread = threading.Thread(target=thread_function, args=('green',))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # n = int(input("Enter the number of slots inside the fitting room: "))
    # b = int(input("Enter the number of blue threads: "))
    # g = int(input("Enter the number of green threads: "))
    n, b, g = 5, 10, 7
    simulate_fitting_room(n, b, g)
