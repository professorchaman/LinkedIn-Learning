"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()
        
    def is_empty(self):
        return not self.items
    
    def enqueue(self,item):
        return self.items.append(item)
        
    def dequeue(self):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)
    

if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("A")
    q.enqueue("D")
    q.enqueue("F")
    print(q)
