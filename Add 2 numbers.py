# #leetcode:

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def addTwoNumbers(self, l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     A=""
#     B=""
#     ln=ListNode(l1)
#     while ln!=None:
#         A+=str(ln.val)
#         ln=ln.next
#     ln=ListNode(l2)
#     while ln!=None:
#         B+=str(ln.val)
#         ln=ln.next
#     A=A[::-1]
#     B=B[::-1]
#     C=int(A)+int(B)
#     C=str(C)
#     C=C[::-1]
#     ln=ListNode()
#     for i in C:
#         ln=ListNode(i,ListNode)
#         ln=ln.next
#     return ln

A="12345"
B="54321"
A=(A[::-1])
B=(B[::-1])
C=int(A)+int(B)
C=str(C)
print(C)