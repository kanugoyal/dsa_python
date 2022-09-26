#Finding middle element in a linked list

from tkinter import N


class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    #function to inset node 
    def insert_node(self, data):        
        node = Node(data,self.head)      # allocate node and put data and link list to new node
        self.head = node                   # point head to new node
        return

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_node(data)

    def print_node(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '>>'
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def middle_ele(self):
        if self.head != None:
            len = self.get_length()

            mid = len // 2

            itr = self.head
            while mid:
                itr = itr.next
                mid = mid - 1
                print(itr.data)


if __name__ == '__main__':
    ll = LinkedList()
   # ll.insert_node(5)
   # ll.print_node()
   # ll.insert_node(6)
   # ll.print_node()
    ll.insert_values([8,2,3])
    ll.print_node()
    ll.middle_ele()
    