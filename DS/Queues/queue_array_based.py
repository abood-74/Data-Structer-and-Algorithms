class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class Queue:
    """FIFO queue implementation using a Python list as underlying storage."""
    
    def __init__(self,capacity = 10) -> None:
        """Create an empty queue."""
        self._data = [None] * capacity
        self._size = 0
        self._front = 0
        self._rear = 0
        
    
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and return the ﬁrst element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None                  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self,e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2*len(self._data))
            
        self._data[self._rear] = e
        self._rear = (self._rear+1) % len(self._data)
        self._size += 1
    
    def _resize(self,cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
        self._rear = self._size -1


if __name__ == "__main__":
        q = Queue()
        for i in range(20):
            q.enqueue(i)
        
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(3)
        q.enqueue(4)
        print(q.first())
        print(q.dequeue())
        print(q.first())
        print(len(q))
        print(q.dequeue())
        print(len(q))
        q.dequeue()
        print(q.is_empty())
        q.dequeue()
        print(q.is_empty())
        
    
    