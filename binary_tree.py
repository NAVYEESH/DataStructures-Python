class Binary_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return 
        if data<self.data:
            # add in left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_tree(data)
        else:
            #right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_tree(data)
    def in_order(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order()
        return elements
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left: 
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self
        
def bulid_tree(elements):
    root=Binary_tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers=[17,4,8,3,56,18,34]
    numbers_tree=bulid_tree(numbers)
    print(numbers_tree.in_order())
    numbers_tree.delete(18)
    print(numbers_tree.in_order())
    print(numbers_tree.search(34))