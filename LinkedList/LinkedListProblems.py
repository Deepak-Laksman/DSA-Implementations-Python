# Reverse a Linkedlist

def revereList(head):
    current = head
    previous = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    head = previous
    return head

# Reverse a LinkedList using Recursion

current = node
def reverseLinkedListReverse(previous = None, current = None):
    if current is None and previous is not None:
        head = previous
        return head
    elif current is None:
        return
    reverseLinkedListReverse(previous, current)
    temp = current.next
    current.next = previous
    previous = current
    current = temp

# Print values in LinkedList using Recursion

def printLinkedListForward(node):
    if node is None:
        print()
        return
    print(node.val, end = " ")
    printLinkedListForward(node.next)

def printLinkedListReverse(node):
    if node is None:
        return
    printLinkedListReverse(node.next)
    print(node.val, end = " ")

# Flatten and sort linked list of linked lists into one linked list.

class ListNode:
    def __init__(self, val = None, bottom = None):
        self.val = val
        self.bottom = bottom

def mergeTwoLists(list1, list2):
    temp = ListNode()
    result = temp
    while list1 and list2:
        if list1.val < list2.val:
            temp.bottom = list1
            list1 = list1.bottom
            temp = temp.bottom
        else:
            temp.bottom = list2
            list2 = list2.bottom
            temp = temp.bottom
    if list1 is not None:
        temp.bottom = list1
    else:
        temp.bottom = list2
    return result


def flatten(linkedList):
    if not linkedList or not linkedList.next:
        return linkedList
    linkedList.next = flatten(linkedList.next)
    linkedList = mergeTwoLists(linkedList, linkedList.next)
    return linkedList