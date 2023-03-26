import ctypes

class DynamicArray:
    """A dynamic array class akin to a simpliﬁed Python list."""
    
    def __init__(self) -> None:
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array
        
    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    
    def __getitem__(self,k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                                # retrieve from array
    
    def append(self,obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                    # not enough room
            self._resize(2*self._capacity)               # so double capacity
        self._A[self._n] = obj                                   
        self._n += 1
    
    def _resize(self,c):                                 # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                          # new (bigger) array
        for k in range(self._n):                         # for each existing value
            B[k] = self._A[k]                                   
        self._A = B                                      # use the bigger array
        self._capacity = c
        
    def _make_array(self, c):                            # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( )
    
    def remove(self , idx):
        if not 0<=idx < self._n:
            raise IndexError("Invalid index")
       
        for i in range(idx , self._n-1):                 # move elements to the left
            self._A[i]=self._A[i+1]

        self._n -=1
        if self._n < self._capacity//4:
            self._resize(self._capacity//2)
    
    def delete(self,num):                               # delete the first occurence of num
        for i in range(self._n):
            v=self._A[i]
            if v == num:
                self.remove(i)
                return True
        return False

    def find(self , num):
        for i in range(self._n):
            v=self._A[i]
            if v == num:
                return i
        return -1
    def __str__(self):
        return str(self._A[:self._n])

if __name__ == "__main__":
    
    L = DynamicArray()
    for i in range(10):
        L.append(i)
    print(L)
    
    print(L)
    L.remove(5)
    print(L)
    
    print(L)
    L.delete(5)
    print(L)
    print(L.find(5))
    print(L.find(6))
    print(L[7])