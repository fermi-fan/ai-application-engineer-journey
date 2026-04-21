queue = []

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueuing 1, 2, 3:", queue)

# Dequeue elements
dequeued_element = queue.pop(0)
print("Dequeued element:", dequeued_element)
print("Queue after dequeuing an element:", queue)

# Peek
front_element = queue[0]
print("Front element:", front_element)

# isEmpty
is_empty = len(queue) == 0
print("Is the queue empty?", is_empty)

# Size
print("Queue size:", len(queue))


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(sefl, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Create a queue instance
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print("Queue after enqueuing 1, 2, 3:", myQueue.queue)
print("Dequeued element:", myQueue.dequeue())
print("Queue after dequeuing an element:", myQueue.queue)
print("Front element:", myQueue.peek())
print("Is the queue empty?", myQueue.isEmpty())
print("Queue size:", myQueue.size())    