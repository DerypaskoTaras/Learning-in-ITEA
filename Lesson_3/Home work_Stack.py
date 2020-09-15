class Stack_:

    def __init__(self):
        self.items = []

    def empty_stack(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0, item)

    def pop(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print('Error. Stack is empty.')

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            print('Error. Stack is empty.')

    def size_stack(self):
        return len(self.items)
