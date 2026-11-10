class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        print(element, "added to queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue.pop(0), "removed from queue")

    def display(self):
        print("Queue:", self.queue)


# Create queue
q = Queue()

# Insert elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Display queue
q.display()

# Remove element
q.dequeue()

# Display again
q.display()