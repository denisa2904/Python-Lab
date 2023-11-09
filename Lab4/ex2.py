class Queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    def __str__(self):
        return str(self.queue)