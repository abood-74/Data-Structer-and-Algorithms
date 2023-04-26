from hash_map_base import HashMapBase
from unsorted_map import UnsortedTableMap
class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""
    
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        
        if bucket is None:
            # no match found
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]  # may raise KeyError
    
    def _bucket_setitem(self,j, k, v):
        if self._table[j] is None:
            # bucket is new to the table
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v  # key was new to the table
        if len(self._table[j]) > oldsize:
            # increase overall map size
            self._n += 1
    
    def _bucket_delitem(self,j, k):
        bucket = self._table[j]
        if bucket is None:
            # no match found
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]  # may raise KeyError
    
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                # a nonempty slot
                for key in bucket:
                    yield key
                    
if __name__ == "__main__"  :              
    # Create a new instance of the ChainHashMap class
    hash_map = ChainHashMap()

    # Set a key-value pair in the hash map
    hash_map["key1"] = "value1"

    # Get the value of a key in the hash map
    print(hash_map["key1"])  # expected output: "value1"

    # Delete a key-value pair from the hash map
    del hash_map["key1"]

    # Try to get the value of a deleted key
    try:
        print(hash_map["key1"])
    except KeyError as e:
        print(str(e))  # expected output: "KeyError: 'key1'"

    # Try to delete a key that does not exist
    try:
        del hash_map["key1"]
    except KeyError as e:
        print(str(e))  # expected output: "KeyError: 'key1'"

    # Test the length of the hash map
    print(len(hash_map))  # expected output: 0

    # Set multiple key-value pairs in the hash map
    hash_map["key1"] = "value1"
    hash_map["key2"] = "value2"
    hash_map["key3"] = "value3"
    
    # Test the length of the hash map again
    print(len(hash_map))  # expected output: 3

    # Test iteration over the hash map
    for key in hash_map:
        print(key)  # expected output: "key1", "key2", "key3"

    # Test deleting a key-value pair from the hash map using iteration
    for key in hash_map:
        if key == "key2":
            del hash_map[key]

    # Test the length of the hash map after deleting a key-value pair
    print(len(hash_map))  # expected output: 2

    # Test getting the value of a key that does not exist
    try:
        print(hash_map["key2"])
    except KeyError as e:
        print(str(e))  # expected output: "KeyError: 'key2'"

