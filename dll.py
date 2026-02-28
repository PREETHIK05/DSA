class Node:
       def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        n=self.head
        while n.next is not None:
             n=n.next
        n.next=newnode
        newnode.prev=n
    def add_after(self,x,data):
        newnode=Node(data)
        if self.head is None:
             newnode.next=self.head
             self.head=newnode
             return
        n=self.head
        while n is not None:
            if x==n.data:
                newnode.next=n.next
                newnode.prev=n
                if n.next is not None:
                    n.next.prev = newnode
                n.next = newnode
                return
            n=n.next
        print("element not found")
    def add_before(self,x,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        n=self.head 
        while n.next is not None:
              if x==n.next.data:
                newnode.next=n.next# first two commands are for adding the new node always do this first 
                newnode.prev=n
                n.next=newnode
                newnode.next.prev = newnode
                return
              n=n.next
        print("element not found")
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty cant delete the element")
            return
        self.head=self.head.next
    def delete_end(self):
        if self.head is None:
            print("linked list is empty cant delete the element")
            return
        if self.head.next is None:
            self.head = None
            return
        n=self.head
        while n.next is not None:#to get  last element 
            n=n.next
        n.prev.next=None     
    def delete_anywhere(self,data):
        if self.head is None:
            print("linked list is empty cant delete the element")
            return
        if self.head.next is None:
            self.head = None
            return
        n=self.head 
        while n is not None:#You don’t need to look at n.next, because you can access both neighbors from n itself.
            if n.data==data:
                if n.next is not None:
                   n.next.prev=n.prev
                   return
                if n.prev is not None:
                    n.prev.next = n.next
                    return
        print("element not found")
    def display_forward(self):
        if self.head is None:
            print("linked list is empty")
            return
        n=self.head
        while n is not None:
                print(n.data, end=" -> ")
                n=n.next
        print("NONE")
    def display_backward(self):
        if self.head is None:
            print("linked list is empty")
            return
        n=self.head
        while n.next is not None:
                n=n.next
        while n is not None:
             print(n.data,end="-->")
             n = n.prev
        print("none")
l1=dll()
l1.add_begin(15)
l1.add_end(25)
l1.add_after(25,50)
l1.add_after(50,89)
l1.display_forward()
l1.display_backward()

      






