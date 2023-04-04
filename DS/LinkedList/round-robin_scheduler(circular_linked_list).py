class CircularQueue:
    
    class _Node:
        """
        Internal class that represents a node in the circular queue.
        """
        __slots__ = "_val", "_next"
        
        def __init__(self, val, next_node=None):
            """
            Initializes a new _Node object with the given value and next node reference.

            Args:
                val: The value to be stored in the node.
                next_node: The reference to the next node in the queue. Default value is None.
            """
            self._val = val
            self._next = next_node
            
    def __init__(self):
        """
        Initializes a new CircularQueue object.
        """
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """
        Returns the number of elements in the circular queue.
        """
        return self._size

    def is_empty(self):
        """
        Returns True if the circular queue is empty, False otherwise.
        """
        return self._size == 0
    
    def first(self):
        """
        Returns the value of the first element in the circular queue without removing it.

        Raises:
            Exception: If the circular queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        head = self._tail._next
        return head._val
    
    def dequeue(self):
        """
        Removes and returns the first element from the circular queue.

        Raises:
            Exception: If the circular queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._val
    
    def enqueue(self, e):
        """
        Adds a new element to the end of the circular queue.

        Args:
            e: The value of the element to be added.
        """
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1
        
    def rotate(self):
        """
        Rotates the circular queue by moving the tail reference to the next element.
        """
        if self._size > 0:
            self._tail = self._tail._next

# Tests
q = CircularQueue()
assert len(q) == 0
assert q.is_empty() == True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
assert len(q) == 3
assert q.is_empty() == False
assert q.first() == 10

assert q.dequeue() == 10
assert len(q) == 2
assert q.first() == 20

q.rotate()
assert q.first() == 30
