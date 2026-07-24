class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a3 = Node(4)
a2 = Node(2, a3)
a1 = Node(1, a2)

b3 = Node(4)
b2 = Node(3, b3)
b1 = Node(1, b2)

def merge(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1 != None:
        tail.next = list1
    if list2 != None:
        tail.next = list2
    return dummy.next

def printnode(head):
    while head != None:
        print(head.val, end = " -> ")
        head = head.next
    print("None")

printnode(merge(a1, b1))