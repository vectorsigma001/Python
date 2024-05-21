"""
Daemon threads run in the background and are killed when the main program exits.
They are useful for background tasks that should not prevent the program from exiting.
"""
import threading
import time

def background_task():
    while True:
        print("Background task is running...")
        time.sleep(2)

# Create a daemon thread
daemon_thread = threading.Thread(target=background_task)
daemon_thread.setDaemon(True)

# Start the daemon thread
daemon_thread.start()

time.sleep(5)
print("Main thread is exiting.")

"""
Background task is running...
Background task is running...
Background task is running...
Background task is running...
Main thread is exiting.
"""
