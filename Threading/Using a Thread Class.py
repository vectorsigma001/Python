# You can also create a custom thread class by subclassing threading.Thread:

import threading
import time

class PrintNumbersThread(threading.Thread):
    def __init__(self, prefix, count):
        threading.Thread.__init__(self)
        self.prefix = prefix
        self.count = count

    def run(self):
        for i in range(1, self.count + 1):
            time.sleep(1)
            print(f"{self.prefix} Number: {i}")

# Create and start a custom thread
thread = PrintNumbersThread("CustomThread", 5)
thread.start()

# Wait for the thread to complete
thread.join()

print("Custom thread has finished execution.")

"""
CustomThread Number: 1
CustomThread Number: 2
CustomThread Number: 3
CustomThread Number: 4
CustomThread Number: 5
Custom thread has finished execution.
"""
