class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        self.prev=None
class double_ll:
    def __init__(self):
        self.head=None
    def print_ll(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def print_reverse(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.prev
    def insert_begin(self ,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head.prev=new_node
            self.head=new_node
    def insert_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
            new_node.prev=n

dl1=double_ll()
dl1.insert_begin(20)
dl1.insert_begin(34)
dl1.insert_end(56)
dl1.insert_begin(40)
dl1.insert_begin(210)
dl1.print_ll()
dl1.print_reverse()