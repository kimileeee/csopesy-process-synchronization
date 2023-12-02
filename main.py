import threading
import time
from fitting_room import run_thread, FittingRoom

def simulate_fitting_room(n, b, g):
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

if __name__ == "__main__":
    # while True:
    #     n = int(input("Number of slots: "))
    #     b = int(input("Number of blue threads: "))
    #     g = int(input("Number of green threads: "))
        
    #     if (n > 0 and b >= 0 and g >= 0):
    #         break
    #     else:
    #         print("Invalid input.")

    n, b, g = 5, 10, 7
    # n, b, g = 5, 10, 0
    # n, b, g = 5, 0, 7

    if (b==0 and g==0):
        print("No threads. Exiting...")
    else:
        simulate_fitting_room(n, b, g)

    