class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"

def reverseBetween(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: ListNode
    """
    if left == right:
        return head
    node=ListNode(0,head)
    node=node.next
    A=[]
    B=[]
    i=1
    while(node):
        if i>=left and i<=right:
            A.append(node.value)
        else:
            B.append(node.value)
        node=node.next
        i+=1
    A=A[::-1] #reverse korar jonno
    left-=1
    right-=1
    i=0
    a=0
    b=0
    node=ListNode(0,head)
    node=node.next
    n=len(A)+len(B)
    while i<n:
        if i>=left and i<=right:
            node.value=A[a]
            node=node.next
            a+=1
        else:
            node.value=B[b]
            node=node.next
            b+=1
        i+=1
    return head

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head






# Example usage
values = [1, 2, 3, 4, 5]
linked_list = create_linked_list(values)
linked_list=reverseBetween(linked_list,2,4)

# Printing the linked list
current = linked_list
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next
