from doubly_linkedlist import _DoublyLinkedBase

class PositonalList(_DoublyLinkedBase):
    """A positional list container based on a doubly linked list."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self,container,node):
            """Constructor should not be called by user."""
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)


    def _validate(self,p):
        """Return node at position p, or raise appropriate error if invalid."""
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self,node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)
        
    def first(self):
        """Return the first Position in the list (or None if empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None if empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self,p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self,p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements in the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def _insert_between(self,e,predecessor,successor):
        """Add element e between two existing nodes and return new Position."""
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)
    
    def add_first(self,e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e,self._header,self._header._next)
    
    def add_last(self,e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e,self._trailer._prev,self._trailer)
    
    def add_before(self,p,e):
        """Insert element e into the list just before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e,original,original._prev)
    
    def add_after(self,p,e):
        """Insert element e into the list just after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e,original,original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        node = self._validate(p)
        return self._delete_node(node)
    
    def replace(self,p,e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    


if __name__ == '__main__':
    # create an empty positional list
    my_list = PositonalList()
    
    # add elements to the list
    my_list.add_first(1)
    my_list.add_last(2)
    my_list.add_after(my_list.first(), 3)
    
    # print the elements of the list
    for elem in my_list:
        print(elem)
        
    # delete an element from the list
    my_list.delete(my_list.last())
    
    # print the updated elements of the list
    for elem in my_list:
        print(elem)
        
    # replace an element in the list
    my_list.replace(my_list.first(), 4)
    
    # print the updated elements of the list
    for elem in my_list:
        print(elem)
