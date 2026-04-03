class Node:
   def __init__(self,data):
    self.data=data
    self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode = Node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top is None:
            print("stack is empty")
            return
        n=self.top #Store the current top node (this is the element to be removed)
        self.top=n.next # Move the top pointer to the next node (removes the top element from stack)
        return n.data #Return the data of the removed node
    def peek(self):
        if self.top is None:
            print("stack is empty")
            return
        return self.top.data
    def display(self):
        n=self.top
        while n:
            print(n.data,end="-->")
            n=n.next
        print("none")
    def search (self,key):
        if self.top is None:
            print("stack is empty")
        n=self.top
        while n :
            if (key == n.data):
                print("value found")
                return
            n=n.next
        print("value is not present in the stack")
s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())
s.search(30)
s.display()
    