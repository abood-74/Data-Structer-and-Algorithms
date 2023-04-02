class Stack:
    class _Node:
        __slots__ = "_val", "_next"                             # streamline memory usage

        def __init__(self, val, next):
            """
            Initializes a new node with a value and a reference to the next node.

            """
            self._val = val
            self._next = next

    def __init__(self):
        """
        Initializes a new empty stack.
        """
        self._size = 0
        self._head = None

    def push(self, val: int) -> None:
        """
        Adds a new value to the top of the stack.
        """
        self._head = self._Node(val, self._head)
        self._size += 1

    def pop(self) -> int:
        """
        Removes and returns the value at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        val = self._head._val
        self._head = self._head._next
        self._size -= 1
        return val

    def top(self) -> int:
        """
        Returns the value at the top of the stack, without removing it.
        """
        if not self._head:
            return None

        return self._head._val

    def __len__(self) -> int:
        """
        Returns the number of elements in the stack.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.
        """
        return self._size == 0

    def top(self) -> int:
        """
        Returns the value at the top of the stack.
        Raises:
            Exception: If the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        return self._head._val


if __name__ == '__main__':
    s = Stack()

    # Check if the stack is empty
    print(s.is_empty())  # True

    # Add elements to the stack
    s.push(1)
    s.push(2)
    s.push(3)

    # Check the size of the stack
    print(len(s))  # 3

    # Remove and return elements from the stack
    print(s.pop())  # 3
    print(s.pop())  # 2

    # Get the value at the top of the stack
    print(s.top())  # 1

    # Check if the stack is empty
    print(s.is_empty())  # False

    # Remove the remaining elements from the stack
    print(s.pop())  # 1

    # Check if the stack is empty
    print(s.is_empty())  # True

    # Try to remove an element from an empty stack
    try:
        print(s.pop())
    except Exception as e:
        print(e)  # "Stack is empty"
