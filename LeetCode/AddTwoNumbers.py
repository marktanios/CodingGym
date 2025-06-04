class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getNumberFromLL(ll):
    counter = 0
    total = 0
    while ll:
        total += ll.val * (10 ** counter)
        ll = ll.next
        counter += 1
    return total

def listToLinkedList(lst):
    if not lst:
        return None

    lst = lst[::-1]
    head = ListNode(int(lst[0]))
    current = head

    for val in lst[1:]:
        current.next = ListNode(int(val))
        current = current.next

    return head

def addTwoNumbers(l1, l2):
    l1_number = getNumberFromLL(l1)
    l2_number = getNumberFromLL(l2)

    sum = l1_number + l2_number
    str_sum = str(sum)
    ll = listToLinkedList(str_sum)
    return ll

def printLinkedList(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == '__main__':
    l1 = listToLinkedList([2, 4, 3])
    l2 = listToLinkedList([5, 6, 4])
    output = addTwoNumbers(l1, l2)
    printLinkedList(output)
