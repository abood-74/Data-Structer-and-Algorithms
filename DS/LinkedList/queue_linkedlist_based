class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_val', '_next'

        def __init__(self, val, next):
            self._val = val
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._val

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        val = self._head._val
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return val

    def enqueue(self, val):
        """Add an element to the back of queue."""
        newest = self._Node(val, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


if __name__ == '__main__':
    q = LinkedQueue()
    print(q.is_empty())
    # True

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(len(q))
    # 3

    print(q.dequeue())
    # 1

    print(q.dequeue())
    # 2

    print(q.first())
    # 3

    print(q.is_empty())
    # False

    print(q.dequeue())
    # 3

    print(q.is_empty())
    # True

    try:
        q.dequeue()
    except Exception as e:
        print(str(e))
    # Queue is empty
