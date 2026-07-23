class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

def rev(head):
    prev = None
    current = head
    while current != None:
        n = current.next
        current.next = prev
        prev = current
        current = n
    return prev

def printnode(head):
    while head != None:
        print(head.val, end = "->")
        head = head.next
    print("None")

head = n1
new_head = rev(head)
printnode(new_head)