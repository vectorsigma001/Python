# When multiple threads modify shared data, 
# you need to synchronize access to prevent data corruption.
# This can be done using locks.
import threading

lock = threading.Lock()
shared_data = 0

def increment():
    global shared_data
    for _ in range(100000):
        with lock:
            shared_data += 1

threads = []
for i in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final value of shared_data: {shared_data}")

# Final value of shared_data: 1000000

