class Empty(Exception):
    """Error attempting to access an element from an empty container."""
class Deque:
    """Double-ended queue (deque) implementation using a Python list as underlying storage."""
    
    def __init__(self, capacity=1):
        """Create an empty deque."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._rear = 0
        
    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size
    
    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]
    
    def last(self):
        """Return (but do not remove) the element at the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._rear - 1]
    
    def enqueue_first(self, e):
        """Add an element to the front of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        
    def enqueue_last(self, e):
        """Add an element to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[self._rear] = e
        self._rear = (self._rear + 1) % len(self._data)
        self._size += 1
        
    def dequeue_first(self):
        """Remove and return the first element of the deque (i.e., FIFO).
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def dequeue_last(self):
        """Remove and return the last element of the deque (i.e., LIFO).
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        self._rear = (self._rear - 1) % len(self._data)
        answer = self._data[self._rear]
        self._data[self._rear] = None
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1 ) % len(self._data)
        
        self._rear = self._size
        self._front = 0
    
    
    
    
    
    
if __name__ == "__main__":
    
    # Create a deque and add elements
    d = Deque()
    d.enqueue_last(1)
    d.enqueue_last(2)
    d.enqueue_last(3)
    d.enqueue_first(0)

    # Test the deque size and elements
    print(len(d))   # Output: 4
    print(d.first())    # Output: 0
    print(d.last())     # Output: 3

    # Remove elements from the deque
    d.dequeue_first()
    d.dequeue_last()

    # Test the deque size and elements again
    print(len(d))   # Output: 2
    print(d.first())    # Output: 1
    print(d.last())     # Output: 2

    # Add more elements to the deque
    d.enqueue_first(-1)
    d.enqueue_last(4)

    # Test the deque size and elements again
    print(len(d))   # Output: 4
    print(d.first())    # Output: -1
    print(d.last())     # Output: 4

            
            
            

    
