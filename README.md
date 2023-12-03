# CSOPESY Project 2: Process Synchronization

#### Synchronization Technique:

The fitting room simulation utilizes the Semaphore synchronization technique. These are used to control access to shared resources, ensuring that only a specified number of threads can access a critical section at a time.

#### List of Variables for Synchronization and Their Corresponding Use:

1. **`slots` (Semaphore)**:

   - **Use**: Controls access to the available slots in the fitting room.
   - **Initialization**: The number of slots (`n`) is set during the creation of the `FittingRoom` instance.
2. **`mutex` (Semaphore)**:

   - **Use**: Provides mutual exclusion to prevent race conditions.
   - **Initialization**: A binary semaphore initialized to 1.
3. **`turnstile` (Semaphore)**:

   - **Use**: Coordinates which color thread is allowed to enter the fitting room. This is to prevent starvation in the program.
   - **Initialization**: A binary semaphore initialized to 1.

#### Code Sections:

##### A. `FittingRoom` Class Initialization:

```python
def __init__(self, n):
    self.n_slots = n
    self.slots = threading.Semaphore(n)
    self.mutex = threading.Semaphore(1)
    self.turnstile = threading.Semaphore(1)
    self.current_color = None
    self.running_threads = []
```

This section initializes the `FittingRoom` class with semaphores (`slots`, `mutex`, `turnstile`), the other relevant information to the object such as `current_color` variable, and an empty list for running threads.

##### B. `enter_fitting_room` Method:

```python
def enter_fitting_room(self, thread):
    self.running_threads.append(thread)
    while True:
        self.mutex.acquire()
        if self.current_color is None:
            # ... (Thread is the first to enter)
        elif self.current_color == thread.color:
            # ... (Thread matches current color and enters)
        else:
            # ... (Thread waits for the fitting room to be available)
        self.mutex.release()
        time.sleep(1)
```

This method manages the entry of threads into the fitting room, ensuring proper synchronization based on the current color and available slots.

##### C. `exit_fitting_room` Method:

```python
def exit_fitting_room(self, thread):
    self.mutex.acquire()
    self.slots.release()
    self.running_threads.remove(thread)
    # ... (Check if the fitting room is empty and update current color)
    self.mutex.release()
```

This method handles the exit of threads from the fitting room, releasing a slot and updating the current color if necessary.

### Running the Simulation:

To run the fitting room simulation, execute the `main.py` script and follow the prompts to input the number of slots, blue threads, and green threads.

**Note**: Ensure that you have Python installed on your system.

```bash
python main.py
```

## Contributors

This project is in partial fulfillment of the course CSOPESY for Term 1, A.Y. 2023 - 2024. Listed below are the contributors to this project:

- [Kim Williame A. Lee](https://github.com/kimileeee) (S12)
- [Criscela Ysabelle Racelis](https://github.com/cyaracelis) (S12)
