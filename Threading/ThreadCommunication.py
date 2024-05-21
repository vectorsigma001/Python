# Threads can communicate using thread-safe data structures like queues.
import threading
import queue
import time

def producer(q):
    for i in range(5):
        item = f"item {i}"
        q.put(item)
        print(f"Produced {item}")
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Signal the consumer to exit
consumer_thread.join()

print("Producer and consumer threads have finished execution.")

"""
Produced item 0
Consumed item 0
Produced item 1
Consumed item 1
Produced item 2
Consumed item 2
Produced item 3
Consumed item 3
Produced item 4
Consumed item 4
Producer and consumer threads have finished execution.
"""
