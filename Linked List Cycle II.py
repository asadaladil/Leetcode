class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Helper function to create a linked list with a cycle for testing
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for index, value in enumerate(values[1:], 1):
        current.next = ListNode(value)
        current = current.next
        if index == pos:
            cycle_node = current

    if cycle_node:
        current.next = cycle_node

    return head
def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or head.next==None:
        return head
    index={}
    i=0
    while head:
        if head in index:
            return head
        index[head]=i
        i+=1
        head=head.next
# Example usage
values = [1, 2, 3, 4, 5]
pos = 2  # The cycle starts at the node with value 3
head = create_linked_list_with_cycle(values, pos)

print(detectCycle(head))
#print("Has cycle:", has_cycle(head))  # Output: True



