class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def __str__(self):
        return str(self.stack)