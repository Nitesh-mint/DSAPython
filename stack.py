class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == [] #returns true if the self.item is empty
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def printStack(self):
        print(self.items[::-1])
