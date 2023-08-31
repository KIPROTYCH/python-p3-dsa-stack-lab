class Stack:
    def __init__(self, items=None, limit=100):
        """Initialize a new stack instance."""
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack."""
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return None  # No action if the stack is full

    def pop(self):
        """Pop an item from the stack."""
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None  # Return None if the stack is empty

    def peek(self):
        """Peek at the top item of the stack without removing it."""
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None  # Return None if the stack is empty

    def size(self):
        """Get the number of items in the stack."""
        return len(self.items)

    def full(self):
        """Check if the stack is full."""
        return len(self.items) == self.limit

    def search(self, target):
        """Search for an item in the stack and return its distance from the top."""
        try:
            index = self.items[::-1].index(target)  # Reverse the items list to search from the top
            return len(self.items) - index  # Calculate distance from the top
        except ValueError:
            return None  # Return None if the item is not found
