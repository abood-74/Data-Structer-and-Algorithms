"""Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

"""


class MyCircularQueue:

    def __init__(self, k: int):
        self._data = [None] * k
        self._size = 0
        self._front = 0
        self._rear = 0
        self._cap = k

    def enQueue(self, e: int) -> bool:
        
        if self._size == self._cap:
            return False
            
        self._data[self._rear] = e
        self._rear = (self._rear + 1) % self._cap
        self._size += 1
        return True
    
    def deQueue(self) -> bool:
        
        if self.isEmpty():
            return False
        answer = self._data[self._front]
        self._data[self._front] = None                  # help garbage collection
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return True

    def Front(self) -> int:
        
        if self.isEmpty():
            return -1
        return self._data[self._front]

    def Rear(self) -> int:
         
        if self.isEmpty():
            return -1
        return self._data[self._rear-1]

    def isEmpty(self) -> bool:
        return self._size == 0
        

    def isFull(self) -> bool:
        return self._size == self._cap
        


if __name__ == "__main__":
    q = MyCircularQueue(3)
    print(q.enQueue(1))
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.enQueue(4))
    print(q.deQueue())
    print(q.Rear())
    print(q.deQueue())
    print(q.Front())
    