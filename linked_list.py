class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'---->',end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_index(self,data,index):
        new_node=node(data)
        n=self.head
        if index==0:
            new_node.ref=self.head
            self.head=new_node
        else:
            for i in range(0,index-1):
                if n is not None:
                    n=n.ref
                else:
                    raise IndexError("index out of bounds")
            new_node.ref=n.ref
            n.ref=new_node
    def delete_begin(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        n=self.head
        if self.head is None:
            print("Linkedlist is empty")
        elif self.head.ref is None:
            self.head=None
        else:
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

ll1=linkedlist()  
ll1.add_begin(30)
ll1.add_begin(10)
ll1.add_end(33)
ll1.add_begin(60)
ll1.add_index(80,3)
ll1.delete_begin()
ll1.delete_end()
ll1.print_ll()