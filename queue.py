stock_price_queue = []
stock_price_queue.insert(0,131.10)
stock_price_queue.insert(0,132.12)
stock_price_queue.insert(0,135)
print(stock_price_queue)

from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(10)
print(q)
q.pop()
print(q)

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.size())
print(pq.dequeue())
print(pq.dequeue())