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

    def delete(self,val):
        if val<self.data:
            if self.left:
             self.left = self.left.delete(val)

        elif val>self.data:
            if self.right:
             self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

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
    
    
    number_tree = build_tree([10,5,8,22,15,14,17,18,19])
    print(number_tree.in_order_traversal())
    number_tree.delete(17)
    number_tree.delete(8)
    print(number_tree.in_order_traversal())
    