import threading
import random
from FittingRoom import FittingRoom
from CustomThread import BlueThread, GreenThread
# from FittingRoomNew import FittingRoom

def simulate_fitting_room(n, b, g):
    
    fitting_room = FittingRoom(n)

    blue_threads = [BlueThread(i, fitting_room) for i in range(b)]
    green_threads = [GreenThread(i, fitting_room) for i in range(g)]

    all_threads = blue_threads + green_threads
    # random.shuffle(all_threads)

    (print(thread.color + str(thread.id)) for thread in all_threads)

    for thread in all_threads:
        thread.start()

    for thread in all_threads:
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

    # n, b, g = 5, 10, 7
    n, b, g = 5, 10, 0
    # n, b, g = 5, 0, 7

    if (b==0 and g==0):
        print("No threads. Exiting...")
    else:
        simulate_fitting_room(n, b, g)

    