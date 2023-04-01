class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Stack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self,capacity = 1) -> None:
        """Create an empty stack."""
        self._data = [None] * capacity
        self._size = 0
        self._top = -1
        self._capacity = capacity
        

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Return True if the stack is empty."""
        if self._size  == self._capacity:
            self._resize(2 * self._capacity)
        
        
        self._top += 1
        self._data[self._top] = e
        self._size +=1
        

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._top]


    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).    
        
        Raise Empty exception if the stack is empty.
        """
        
        if self.is_empty():
            raise Empty('Stack is empty')
        number = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        self._size -= 1

        if self._size <= self._capacity // 4 and len(self._data) > 1:
            self._resize(self._capacity //2)
        return number
    
    def _resize(self,cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = old[i]
        self._capacity = cap
    
        


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
        print(s._data)
        print(len(s))
        s.pop()
        print(s.is_empty())
        print(s._data)
        s.pop()
        print(s._data)
        print(s.is_empty())
