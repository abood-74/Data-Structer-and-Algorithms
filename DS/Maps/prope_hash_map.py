from hash_map_base import HashMapBase
class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""

    # Sentinel object used to mark deleted slots
    _AVAIL = object()

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j  # mark this as first available slot
                if self._table[j] is None:
                    return (False, first_avail)  # search has failed
            elif k == self._table[j]._key:
                return (True, j)  # found a match
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        """Return the value associated with key k in bucket at index j."""
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f'Key Error: {repr(k)}')
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        """Assign value v to key k in bucket at index j, or insert new item if not found."""
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self.Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        """Remove item associated with key k in bucket at index j."""
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f'Key Error: {repr(k)}')
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        """Generate an iteration of all keys in the map."""
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

if __name__ == "__main__":
    # Create a new ProbeHashMap instance
    hm = ProbeHashMap()

    # Test __setitem__ and __getitem__
    print("Testing __setitem__ and __getitem__...")
    hm[1] = "One"
    hm[2] = "Two"
    hm[3] = "Three"
    print(hm[1])  # Expected output: "One"
    print(hm[2])  # Expected output: "Two"
    print(hm[3])  # Expected output: "Three"

    # Test __delitem__
    print("\nTesting __delitem__...")
    del hm[2]
    try:
        print(hm[2])  # Expected output: KeyError
    except KeyError as e:
        print(str(e))
    

    # Test __len__
    print("\nTesting __len__...")
    print(len(hm))  # Expected output: 2

    # Test __iter__
    print("\nTesting __iter__...")
    for key in hm:
        print(key)  # Expected output: 1, 3

    # Test clear
    print("\nTesting clear...")
    hm.clear()
    print(len(hm))  # Expected output: 0
