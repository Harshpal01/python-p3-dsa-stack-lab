class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit

    def push(self, value):
        if self.limit is not None and len(self.items) >= self.limit:
         self.items[-1] = value
        else:
         self.items.append(value)
        return self

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    isEmpty = empty  # alias for test compatibility

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == value:
                return len(self.items) - 1 - i
        return -1

    def __str__(self):
        return f"Stack(top -> bottom): {self.items[::-1]}"
