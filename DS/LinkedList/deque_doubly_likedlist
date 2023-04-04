from doubly_linkedlist import _DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):
    # note the use of inheritance
    
    """Double-ended queue implementation based on a doubly linked list."""
    
    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        # real item just after header
        return self._header._next._element
    
    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")
        # real item just before trailer
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self.insert_between(e, self._header, self._header._next) # after header
        
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        # before trailer
        self.insert_between(e, self._trailer._prev, self._trailer)
    
    def delete_first(self):
        """Remove and retuEmptyrn the element from the front of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        # use inherited method
        return self.delete_node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element from the back of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        # use inherited method
        return self.delete_node(self._trailer._prev)
if __name__ == '__main__':
    deque = LinkedDeque()
    assert deque.is_empty() == True
    
    deque.insert_first(1)
    deque.insert_first(2)
    deque.insert_last(3)
    assert deque.first() == 2
    assert deque.last() == 3
    
    deque.delete_last()
    assert deque.last() == 1
    
    deque.delete_first()
    assert deque.first() == 1

