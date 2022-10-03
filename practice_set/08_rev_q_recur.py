from queue import Queue


def reverse_queue(queue: Queue):

	if queue.empty():
		return

	item = queue.queue[0]
	queue.get()

	
	reverse_queue(queue)
	queue.put(item)       ## insertcurrent element at back


def print_queue(queue: Queue):
	while not queue.empty():
		print(queue.queue[0], end=" ")
		queue.get()
	print()


# Driver Code
if __name__ == "__main__":
	q = Queue()
	q.put(56)
	q.put(27)
	q.put(30)
	q.put(45)
	q.put(85)
	q.put(92)
	q.put(58)
	q.put(80)
	q.put(90)
	q.put(100)

	reverse_queue(q)
	print_queue(q)
