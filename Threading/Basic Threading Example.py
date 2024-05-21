# To create and start a thread in Python, you use the threading module:

import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number: {i}")

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

print("Thread has finished execution.")

"""
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Thread has finished execution.
"""
