class Node:
       def __init__(self, data):
        self.data = data
        self.next = None#If the structure is circular never use None for links
class cll:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
            return 
        n=self.head
        while n.next is not self.head :
            n=n.next
        n.next=newnode# Make the last node point to the new node instead of pointing back to the head.
        newnode.next=self.head# Make the new node point to the old head so the circular connection continues.
        self.head = newnode# Update the head reference so the new node becomes the first node of the list.
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
            return 
        n=self.head
        while n.next is not self.head:
            n=n.next
        n.next=newnode
        newnode.next=self.head
    def add_anywhere(self,pos,data):
        newnode=Node(data)
        if pos<0:
            print("invalid position,cant be added")
            return
        if self.head is None:#if linked lsit is empty 
               newnode.next=self.head
               self.head=newnode
               return
        if pos==0:#adding element at the beginning
            n=self.head
            while n.next is not self.head :
                    n=n.next
            n.next=newnode
            newnode.next=self.head
            self.head = newnode
            return
        n=self.head 
        count=0
        while count<pos-1 and n.next is not self.head :
            n=n.next
            count+=1
        if count is not pos-1:
            print("out of range")
            return
        newnode.next=n.next
        n.next=newnode
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.next == self.head:# only one node is present 
            self.head = None
            return
        n=self.head 
        while n.next is not self.head :
            n=n.next
        self.head=self.head.next
        n.next=self.head
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.next == self.head:# only one node is present 
            self.head = None
            return
        n=self.head
        while n.next.next is not self.head:
            n=n.next
        n.next=self.head 
    def delete_anywhere(self,pos):
        if self.head is None:
            print("linked list is empty ")
            return
        if pos<0:
            pritn("invalid position ")
            return
        if pos==0:
            if self.head.next==self.head:
                self.head=None
                return
            n=self.head
            while n.next is not self.head:
                n=n.next
            self.head=self.head.next
            n.next=self.head
            return
        n=self.head
        count=0
        while count<pos-1 and n.next is not self.head:
            n=n.next
            count+=1
        if count is not pos-1 :
            print("invalid index")
            return
        n.next=n.next.next
    def display(self):
        if self.head is None:
            print("linked list is empty")
            return
        n=self.head
        while n.next is not self.head :
            print(n.data,end="-->")
            n=n.next
        print(n.data, end="-->NONE")
l1=cll()
l1.add_begin(50)
l1.add_end(15)
l1.add_anywhere(0,45)
l1.add_anywhere(1,57)
l1.delete_begin()
l1.delete_end()
l1.delete_anywhere(1)
l1.display()
        
        
        
            
        




