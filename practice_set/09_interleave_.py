#Interleave the first half of the queue with second half

from queue import Queue

def interLeaveQueue(q):

	if (q.qsize() % 2 != 0):              # To check the even number of elements
		print("Input even number of integers.")

	s = []
	halfSize = int(q.qsize() / 2)

	for i in range(halfSize):    #put put first half elements into the stack queue
		s.append(q.queue[0])
		q.get()

	while len(s) != 0:
		q.put(s[-1])
		s.pop()

	# dequeue the first half elements of queue and enqueue them back
	for i in range(halfSize):
		q.put(q.queue[0])
		q.get()

	# Again put the first half elements into the stack queue
	for i in range(halfSize):
		s.append(q.queue[0])
		q.get()

	# interleave the elements of queue and stack queue
	while len(s) != 0:
		q.put(s[-1])
		s.pop()
		q.put(q.queue[0])
		q.get()



if __name__ == '__main__':
	q = Queue()
	q.put(1)
	q.put(2)
	q.put(3)
	q.put(4)
	q.put(5)
	q.put(6)
	q.put(7)
	q.put(8)
	q.put(9)
	q.put(10)
	interLeaveQueue(q)
	length = q.qsize()
	for i in range(length):
		print(q.queue[0], end=" ")
		q.get()

