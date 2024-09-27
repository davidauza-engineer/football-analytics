class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        return self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0