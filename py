class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class insert:        
    def insert(data,position):
        if(pos<0):
            print("enter the valid position")
            return
        if(pos==0):
            self.head.next=self.head
            self.head=Node(data)
            return
        mid=0
        current=self.head
        while(current.next,mid<pos-1):
            mid+=1
            current=current.next
        if(current is None):
            print("position is out of bound")
            return
        current.next=data
        data.next=current.next.next
    def display():
        current=self.head
        while(current):
            print(current)
n=Node
d=insert()
d.insert(10,0)
d.insert(20,0)
d.insert(30,1)
d.display()
        
    
