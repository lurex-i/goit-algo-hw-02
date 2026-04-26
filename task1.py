from queue import Queue
import random

queue = Queue()
unique_id = 1

def generate_request():
    global unique_id
    queue.put(unique_id)
    print(f"Request with ID = {unique_id} goes to the queue")
    unique_id += 1

def process_request():
    if not queue.empty():
        request_id = queue.get()
        print(f"We service request with ID = {request_id}")
    else :
        print("There are not requests in the queue.")

for i in range(8):
    for times in range(random.randint(2, 8)):
        generate_request()
    for times in range(random.randint(3, 7)):
        process_request()

# Process any left requests in the queue
while not queue.empty():
    process_request()
