class Node:
    def __init__(self,n):
        self.val=n
        self.next=None

def insert(node,pos,val):
    if node is None:
        return node
    x=1
    curr=node
    while x<pos:
        curr=curr.next
    y=Node(val)
    y.next=curr.next
    curr.next=y

def delete(node,pos):
    curr=node
    s=1
    while s<pos:
        curr=curr.next
    x=curr.next
    curr.next=curr.next.next
    x.next=None
    