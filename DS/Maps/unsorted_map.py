"""This list-based map implementation is simple, but it is not particularly efﬁcient.
Each of the fundamental methods, getitem , setitem , and delitem ,
relies on a for loop to scan the underlying list of items in search of a matching key.
In a best-case scenario, such a match may be found near the beginning of the list, in
which case the loop terminates; in the worst case, the entire list will be examined.
Therefore, each of these methods runs in O(n) time on a map with n items.
"""
from map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""
    
    def __init__(self):
        """Create an empty map."""
        self.table = []

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self.table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error")

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self.table:
            if k == item._key:
                item._value = v
                return
        self.table.append(self.Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self.table)):
            if k == self.table[j]._key:
                self.table.pop(j)
                return
        raise KeyError("Key Error")

    def __len__(self):
        """Return number of items in the map."""
        return len(self.table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self.table:
            yield item._key



# Test cases for UnsortedTableMap

# Create an empty map
map = UnsortedTableMap()

# Test __setitem__ and __getitem__
map['a'] = 1
map['b'] = 2
map['c'] = 3
print(map['a'])  # Expected output: 1
print(map['b'])  # Expected output: 2
print(map['c'])  # Expected output: 3

# Test __len__
print(len(map))  # Expected output: 3

# Test __delitem__
del map['b']
print('b' not in map)  # Expected output: True
print(len(map))  # Expected output: 2

# Test KeyError for nonexistent key
try:
    print(map['d'])
except KeyError as e:
    print(str(e))  # Expected output: "Key Error"
else:
    print("KeyError not raised for nonexistent key")
