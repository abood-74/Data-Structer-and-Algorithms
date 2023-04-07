from positional_list import PositionalList

class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    #------------------------------ nested Item class ------------------------------
    class Item:
        __slots__ = '_value', '_count'  # streamline memory usage

        def __init__(self, e):
            """the user's element"""
            self._value = e
            """access count initially zero"""
            self._count = 0

    #------------------------------- nonpublic utilities -------------------------------
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element() != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        # consider moving...
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            # must shift forward
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                    cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                # delete/reinsert
                self._data.add_before(walk, self._data.delete(p))
    
    #------------------------------- public utilities -------------------------------
    def __init__(self):
        """Create an empty list of favorites."""
        # will be list of Item instances
        self._data = PositionalList()

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        # try to locate existing element
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self.Item(e))  # if new, place at end
        # always increment count
        p.element()._count += 1
        # consider moving forward
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites."""
        # try to locate existing element
        p = self._find_position(e)
        if p is not None:
            # delete, if found
            self._data.delete(p)

    def top(self, k):
        """Generate sequence of not more than k elements of the most frequently accessed elements."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            # element of list is Item
            # report user's element
            yield item._value
            walk = self._data.after(walk)
