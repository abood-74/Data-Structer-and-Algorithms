class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Stack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Return True if the stack is empty."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).    
        
        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

if __name__ == "__main__":
        s = Stack()
        s.push(5)
        s.push(6)
        s.push(3)
        s.push(4)
        print(s.top())
        print(s.pop())
        print(s.top())
        print(s.pop())
        print(len(s))
        s.pop()
        print(s.is_empty())
        s.pop()
        print(s.is_empty())
