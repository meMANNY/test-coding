import threading

counter = 0

lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment_counter) for _ in range(7)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]

print(f"Final counter value: {counter}")

