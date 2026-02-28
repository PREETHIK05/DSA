class Node:#Node stores individual data and a pointer to the next node
# while LinkedList manages the chain of nodes, keeping code clean, modular, and easy to maintain.
    def __init__(self, data):
        self.data = data
        self.next = None
class ll:
    def __init__(self):#self is used as the first parameter in instance methods to refer to the current object. 
                      #It allows methods within the class to access and modify the object's attributes, making each object independent of others.
        self.head = None #initiate the head its complusory
    def add_begin(self,data):
        newnode=Node(data) # creating a new code . must do it for add and delete 
        newnode.next=self.head 
        self.head=newnode 
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head = newnode
            return newnode
        n=self.head
        while n.next is not None:
            n=n.next
        n.next=newnode
    def add_after(self,x,data):
        newnode=Node(data)
        if self.head is None:
            newnode.next=self.head
            self.head=newnode
            return
        n=self.head
        while n is not None:
            if x==n.data:# checking whether given value is equal to value aldready present in linked list 
                break
            n=n.next
        if n is None: # when given node is not present in the linked list 
            print("no such node is present")
        else :
            newnode.next=n.next# tells the new node who comes after it (like we r pointing new node to where the given node was pointing to)
            n.next=newnode #make the current node point to the new node(the node after where we r adding the new node make that node point to new node so it'll be pointing new node)        
    def add_before(self,x,data):
        newnode=Node(data)
        if self.head is None:
            print("List is empty")
            return
        if x==self.head.data:#x is data#self.head.data is data#You must compare same types
            newnode.next=self.head
            self.head=newnode
        else:
            n=self.head
            while n.next is not None:# n = current node, n.next = next node;# Use n for current, n.next when you care about what comes after
               if n.next.data==x:
                break
               n=n.next 
            if n.next is None:
                print("node doesn't exist")
            else:
                newnode.next=n.next# we r pointing to next node where n was pointing before 
                n.next=newnode#connects the previous node n to the new node
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty ,cannot delete elements from it")
            return
        self.head=self.head.next
    def delete_end(self):
        if self.head is None:
            print("linked list is empty ,cannot delete elements from it")
            return
        if self.head.next is None:
            self.head = None
            return
        n=self.head
        while n.next.next is not None:# to get second last node
            n=n.next#second last node
        n.next=None
    def delete_anywhere(self,data):
        if self.head is None:
            print("linked list is empty ,cannot delete elements from it")
            return
        if data==self.head.data:
            self.head=self.head.next
            return
        n=self.head
        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return 
            n = n.next
        print("not found ")  
    def display(self):
        if self.head is None:
            print("ll is empty")
            return
        n=self.head 
        while n is not None:
                print(n.data, end=" -> ")
                n=n.next
        print("NONE")
l1=ll()
l1.add_begin(10)
l1.add_begin(25)
l1.add_end(8)
l1.add_after(25,45)#add 45 after 25 
l1.add_before(25,67)#add before 25
l1.delete_begin()
l1.delete_end()
l1.delete_anywhere(25)
l1.display()
