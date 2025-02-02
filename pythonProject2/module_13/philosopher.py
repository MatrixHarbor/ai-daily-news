import random
import threading
import time

from fork import Fork

class Philosopher(threading.Thread):
    running = True

    # Initialize a philosopher's name, left fork, and right fork
    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        super().__init__()  # Call threading superclass constructor
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    # run() is called by thread’s start() method; starts the thread running
    def run(self):
        while self.running:
            self.think()  # Call think()
            self.eat()    # Call eat()
        print(f"{self.name} is cleaning up.")  # Print cleanup message

    # Make philosopher think for a random number of seconds until hungry
    def think(self):
        # Generate a random number of seconds between 3 and 5
        thinking_time = random.uniform(3, 5)
        print(f"{self.name} is thinking for {thinking_time} seconds.")
        time.sleep(thinking_time)
        print(f"{self.name} is now hungry.")

    # Make philosopher eat for a random number of seconds until thinking again
    def eat(self):
        # Try to acquire left fork
        if self.left_fork.acquire_fork():  # If successful
            try:
                # Try to acquire right fork
                if self.right_fork.acquire_fork():
                    try:
                        # Generate a random eating time between 3 and 5 seconds
                        eating_time = random.uniform(3, 5)
                        print(f"{self.name} is eating for {eating_time} seconds.")  # Print eating time
                        time.sleep(eating_time)
                    finally:
                        # Release right fork
                        self.right_fork.release_fork()
                        print(f"{self.name} has put down his right fork.")
            finally:
                # Release left fork
                self.left_fork.release_fork()
                print(f"{self.name} has put down his left fork.")