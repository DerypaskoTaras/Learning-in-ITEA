class Queue_:

    def __init__(self):
        self.items = []

    def empty_queue(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print('Error. Queue is empty.')

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            print('Error. Queue is empty.')

    def size_queue(self):
        return len(self.items)
