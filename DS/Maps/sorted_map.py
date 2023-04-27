from map_base import MapBase


class SortedMap(MapBase):
    
    
    #----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self,k,low,high):
        
        while low <= high:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k > self._table[mid]._key:
                low = mid + 1
            elif k < self._table[mid]._key:
                high = mid - 1
        return high + 1
    
    #----------------------------- public behaviors -----------------------------
    def __init__(self) -> None:
        self._table = []
        
    def __len__(self):
        return len(self._table)
    
    def __getitem__(self,k):
        j = self._find_index(k,0,len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value
    def __setitem__(self, k,v):
        j = self._find_index(k,0,len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j,self.Item(k,v))
    
    def __delitem__(self, k) -> None:
        j = self._find_index(k,0,len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)
    
    def __iter__(self):
        for item in self._table:
            yield item._key
    
    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key
    
    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None
    
    def find_max(self):
        if len(self._table) > 0:
            return (self._table[len(self._table) - 1]._key,self._table[len(self._table) - 1]._value)
        else:
            return None
    def find_ge(self, k):
        # j is key >= k
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
            
    def find_lt(self, k):
        # j is key >= k
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value) # Note use of j-1
        else:
            return None
            
    def find_gt(self, k):
        # j is key >= k
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
            # advanced past match
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None
            
    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            # find first result
            j = self._find_index(start, 0, len(self._table)-1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
if __name__ == "__main__":
    # create a new sorted map
    sm = SortedMap()

    # test __setitem__ method
    sm[3] = "three"
    sm[1] = "one"
    sm[4] = "four"
    sm[2] = "two"
    print(dict(sm))  # should print {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

    # test __getitem__ method
    print(sm[2])  # should print "two"
    try:
        print(sm[5])  # should raise a KeyError
    except KeyError:
        print("KeyError raised as expected")

    # test __delitem__ method
    del sm[3]
    print(dict(sm))  # should print {1: 'one', 2: 'two', 4: 'four'}
    try:
        del sm[5]  # should raise a KeyError
    except KeyError:
        print("KeyError raised as expected")

    # test __iter__ method
    for k in sm:
        print(k)  # should print 1, 2, 4

    # test __reversed__ method
    for k in reversed(sm):
        print(k)  # should print 4, 2, 1

    # test find_min method
    print(sm.find_min())  # should print (1, 'one')

    # test find_max method
    print(sm.find_max())  # should print (4, 'four')

    # test find_ge method
    print(sm.find_ge(2))  # should print (2, 'two')

    # test find_lt method
    print(sm.find_lt(3))  # should print (2, 'two')

    # test find_gt method
    print(sm.find_gt(2))  # should print (4, 'four')

    # test find_range method
    for k, v in sm.find_range(2, 4):
        print(k, v)  # should print 2 two \n 4 four

