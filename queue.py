class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        newnode=Node(data)
        if self.rear is None:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode
    def dequeue(self):
        if self.front is None:
            print("queue is empty")
            return
        n=self.front #Store the current front node in a temporary variable n
        self.front=n.next #Move the front pointer to the next node (removes front element)
        if self.front is None: #If self.front is None (we removed the last element), we also need to update self.rear to None.
            self.rear = None
    def peek(self):
        if self.front is None:
            print("queue is empty")
            return None
        return self.front.data
    def search(self,key):
        if self.front is None:
            print("queue is empty")
            return
        n=self.front
        while n :
            if (n.data==key):
                return True
            n=n.next
        return False
    def display(self):
        if self.front is None:
            print("queue is empty")
            return
        n=self.front
        while n :
            print(n.data,end="-->")
            n=n.next
        print("none")
q=queue()
q.enqueue(100)
q.enqueue(20)
q.enqueue(50)
q.dequeue()
print(q.peek())
print(q.search(15))
q.display()
