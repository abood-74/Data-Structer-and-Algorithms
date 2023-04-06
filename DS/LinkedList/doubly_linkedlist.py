class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        def __init__(self, element, prev, next_):
            self._element = element
            self._prev = prev
            self._next = next_

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)  # sentinel node at the head
        self._trailer = self._Node(None, None, None)  # sentinel node at the tail
        self._header._next = self._trailer  # connect header to trailer
        self._trailer._prev = self._header  # connect trailer to header
        self._size = 0  # number of elements in the list

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # create new node
        predecessor._next = newest  # link predecessor to new node
        successor._prev = newest  # link successor to new node
        self._size += 1  # increment the size of the list
        return newest

    def _delete_node(self, node):
        """Delete non-sentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor  # link predecessor to successor
        successor._prev = predecessor  # link successor to predecessor
        self._size -= 1  # decrement the size of the list
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element  # return deleted element


# Tests
if __name__ == '__main__':
    # create an empty list
    dll = _DoublyLinkedBase()

    # check if the list is empty
    print(f"Is the list empty? {dll.is_empty()}")  # expected output: True

    # insert elements into the list
    node1 = dll._insert_between(10, dll._header, dll._trailer)
    node2 = dll._insert_between(20, node1, dll._trailer)
    node3 = dll._insert_between(30, dll._header, node1)

    # check the size of the list
    print(f"The size of the list is: {len(dll)}")  # expected output: 3

    # check if the list is empty
    print(f"Is the list empty? {dll.is_empty()}")  # expected output: False

    # delete an element from the list
    deleted_element = dll._delete_node(node2)
    print(f"The deleted element is: {deleted_element}")  # expected output: 20

    # check the size of the list after deletion
    print(f"The size of the list after deletion is: {len(dll)}")  # expected output: 2

    # print the elements in the list
    current = dll._header._next
    print("Elements in the list: ", end="")
    while current != dll._trailer:
        print(current._element, end=" ")
        current = current._next
    # expected output: 10 30
