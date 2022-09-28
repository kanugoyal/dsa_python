class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return       #already exist

        if data <self.data:
            if self.left:
              self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:  
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
             elements += self.right.in_order_traversal()
        

        return elements

    def search(self,val):
        if self.data == val:
            return True

        if val< self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False




def build_tree(elements):
    print("Building tree with :",elements)
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    root = BinarySearchTreeNode(5)
    root.add_child(2)
    root.add_child(9)
    root.add_child(5)

    numbers = [17,4,1,20,9,23,18,34]
    root = build_tree(numbers)
    print(root.in_order_traversal())
    print(root.search(23))
    print(root.search(456))

    countries = ["India","Germany","Usa","China","India","Uk"]
    countries_tree = build_tree(countries)
    print(countries_tree.in_order_traversal())
    print(countries_tree.search("India"))
    print(countries_tree.search("Usa"))
    pass
