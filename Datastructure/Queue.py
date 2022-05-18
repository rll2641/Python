class Queue:
    def __init__(self):
        self.queue = []
    def queue_size(self):
        return len(self.queue)
    def is_empty(self):
        return (self.queue_size() == 0)
    def enqueue(self, num):
        self.queue.append(0, num)
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            return self.queue.pop(0)
    