class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self,head,temp):
        self.head=None
        self.temp=None

    def create(self):
        size=int(input())
        for i in range(size):
            value=int(input())
            newnode = Node(value)
            newnode.next = None

            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode

    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data)
            self.temp=self.temp.next

    def insertmiddle(self):
        position = int(input("Enter "))
        value = int(input("Enter the Value "))
        newnode = Node(value)
        self.temp=self.head
        i=1
        while i < position:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        self.temp.next=newnode
        

obj1=LinkedList(None,None)
obj1.create()
obj1.display()
obj1.insertmiddle()
obj1.display()
