# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry=0
    head=ListNode(-10)
    temp=head
    while (l1 or l2)!=None or carry!=0:
        if l1!=None and l2!=None:
            sm=l1.val+l2.val+carry
            temp.next=ListNode(sm%10)
            carry=int(sm/10)
            temp=temp.next
            l1=l1.next
            l2=l2.next
        elif l1==None and l2!=None:
            sm=l2.val+carry
            temp.next=ListNode(sm%10)
            carry=int(sm/10)
            temp=temp.next
            l2=l2.next
        elif l1!=None and l2==None:
            sm=l1.val+carry
            temp.next=ListNode(sm%10)
            carry=int(sm/10)
            temp=temp.next
            l1=l1.next
        elif l1==None and l2==None:
            if carry!=0:
                temp.next=ListNode(carry)
                carry=0
    return head.next

l1=create_linked_list([9,9,9,9,9,9,9])
l2=create_linked_list([9,9,9,9])
head=addTwoNumbers(l1,l2)
while head:
    print(head.val,end=' ')
    head=head.next

        