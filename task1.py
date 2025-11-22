from queue import Queue
from faker import Faker
from time import sleep

queue = Queue()
fake = Faker()

class Request:
    id_counter = 0

    def __init__(self, name):
        self.name = name
        self.id = Request.id_counter
        Request.id_counter += 1

def generate_request() -> None:
    new_request = Request(fake.name())
    queue.put(new_request)
    print(f"Added request #{new_request.id}: {new_request.name}")

def process_request() -> None:
    if queue.empty():
        print("The queue is empty. No requests to process.")
        return

    request = queue.get()
    print(f"Processing request #{request.id}: {request.name}")

try:
    while True:
        generate_request()
        sleep(0.2) # just for readability
        process_request()
        sleep(0.5) # just for readability

except KeyboardInterrupt:
    print("Program terminated by user.")
