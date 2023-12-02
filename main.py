import threading
import time
from fitting_room import run_thread, FittingRoom
# from fittingroom import run_thread, FittingRoom

# def simulate_fitting_room(n, b, g):
#     fitting_room = FittingRoom(n)
    
#     def run_thread(color):
#         fitting_room.enter_fitting_room(color)
#         time.sleep(1)  # Simulate some activity in the fitting room
#         fitting_room.exit_fitting_room(color)

#     blue_threads = [threading.Thread(target=run_thread, args=('blue',)) for _ in range(b)]
#     green_threads = [threading.Thread(target=run_thread, args=('green',)) for _ in range(g)]

#     all_threads = blue_threads + green_threads
#     for thread in all_threads:
#         thread.start()

#     for thread in all_threads:
#         thread.join()

# def simulate_fitting_room(n, b, g):
    # slots = threading.Semaphore(n)
    # green = threading.Lock()
    # blue = threading.Lock()
    # mutex = threading.Lock()
    # empty = threading.Lock()

if __name__ == "__main__":
    # while True:
    #     n = int(input("Number of slots: "))
    #     b = int(input("Number of blue threads: "))
    #     g = int(input("Number of green threads: "))
        
    #     if (n > 0 and b > 0 and g > 0):
    #         break
    #     else:
    #         print("Invalid input.")

    # simulate_fitting_room(n, b, g)
    n, b, g = 5, 10, 7

    fittingroom = FittingRoom(n)
    threads = []

    for i in range(b):
        threads.append(threading.Thread(target=run_thread, args=(fittingroom.BLUE+str(i), fittingroom.BLUE, fittingroom)))

    for i in range(g):
        threads.append(threading.Thread(target=run_thread, args=(fittingroom.GREEN+str(i), fittingroom.GREEN, fittingroom)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()