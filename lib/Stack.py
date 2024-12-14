class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack, ensuring it doesn't exceed the limit"""
        if len(self.items) >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        """Pop the top item from the stack"""
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it from the stack"""
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the size of the stack"""
        return len(self.items)

    def full(self):
        """Check if the stack is full"""
        return len(self.items) >= self.limit

    def search(self, target):
        """Search for an item in the stack and return its position from the top of the stack"""
        try:
            # Reverse the list to find the position from the top of the stack
            return len(self.items) - self.items[::-1].index(target) - 1
        except ValueError:
            return -1  # Return -1 if the item is not found
