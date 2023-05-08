from binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent = None, left = None, right = None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        
        
        def __init__(self, container, node) -> None:
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other) -> bool:
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer a valid position')
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node else None
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: 
            raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: 
            raise ValueError('left child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
            
            
 
if __name__ == "__main__":
    t = LinkedBinaryTree()
    root = t._add_root(1)
    left = t._add_left(root, 2)
    right = t._add_right(root, 3)

    print(t.root().element())  # expected output: 1
    print(t.parent(left).element())  # expected output: 1
    print(t.parent(right).element())  # expected output: 1
    print(t.left(root).element())  # expected output: 2
    print(t.right(root).element())  # expected output: 3
    print(t.num_children(root))  # expected output: 2
    print(t.num_children(left))  # expected output: 0
    print(t.num_children(right))  # expected output: 0
    print(t._replace(left, 4))  # expected output: 2
    print(t.left(root).element())  # expected output: 4
    print(t._delete(right))  # expected output: 3
    print(t.num_children(root))  # expected output: 1
    print(t.right(root))  # expected output: None
    print(len(t))  # expected output: 2
    print(t.is_root())
     