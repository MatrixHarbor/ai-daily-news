import time

from fork import Fork
from philosopher import Philosopher

def DiningPhilosophers():
    # Create an array of 5 philosopher names
    names = ["Plato", "Aristotle", "Buddha", "Marx", "Nietzsche"]

    # Create 5 Fork objects using a list comprehension
    forks = [Fork() for _ in range(5)]

    philosophers = [
        Philosopher(names[i], forks[i], forks[(i + 1) % 5]) for i in range(5)
    ]

    # start all Philosopher threads (should be non-blocking)
    for philosopher in philosophers:
        philosopher.start()

    # sleep for 10 seconds
    time.sleep(10)

    Philosopher.running = False

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    DiningPhilosophers()