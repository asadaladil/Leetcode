
class Node(object):
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def ret_head(self):
        return self.head

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def add_child(self, parent_value, child_value):
        current = self.head
        while current:
            if current.val == parent_value:
                child_node = Node(child_value)
                current.child = child_node
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(f"Node({current.val})", end="")
            if current.child:
                print(f" -> Child(Node({current.child.val}))", end="")
            print(" <-> ", end="")
            current = current.next
        print("None")

    def print_flat_list(self):
        def print_node(node):
            while node:
                print(f"Node({node.val})", end=" <-> ")
                if node.child:
                    print_node(node.child)
                node = node.next
        print_node(self.head)
        print("None")

# def flatten(head):
#     """
#     :type head: Node
#     :rtype: Node
#     """
#     if not head:
#         return head
#     head2=Node(head.val)
#     head2.prev=None
#     current=head
#     current2=head2
#     node_store=[]
#     while node_store or current:
#         if current==None:
#             if len(node_store)==0:
#                 break
#             # pop kora value Ta neoar jonno ei kaj kora
#             current=node_store.pop()
#             node=Node(current.val)
#             current2.next=node
#             current2.next.prev=current2
#             current2=current2.next
#         elif current.child==None and current.next:
#             node=Node(current.next.val)
#             current2.next=node
#             current2.next.prev=current2
#             current2=current2.next
#             current=current.next
#         elif current.child:
#             if current.next:
#                 node_store.append(current.next)
#             node=Node(current.child.val)
#             current2.next=node
#             current2.next.prev=current2
#             current2=current2.next
#             current=current.child
#         else:
#             current=current.next
#     return head2

# Recursive Form:
def flatten(head):
    if not head:
        return head
    head2=Node(0)
    current=head2
    def flat(Head):
        if Head!=None:
            nonlocal current # bairer variable use korbo tar jonno
            current.next=Node(Head.val)
            current.next.prev=current
            current=current.next

        if Head!=None and Head.child :
            flat(Head.child)
            
        if Head!=None and Head.next:
            flat(Head.next)
            
    flat(head)
    head2=head2.next
    head2.prev=None # 0 ei link list er ongso ta tai bad deoa holo
    return head2

def printed(head):
    while head:
        print(head.val,end=' ')
        head=head.next

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

# Add child nodes
dll.add_child(2, 5)
dll.add_child(3, 6)
dll.add_child(4, 7)

printed(flatten(dll.head))

# Print the list with child nodes
# print("Doubly Linked List with Child Nodes:")
# dll.print_list()

# # Print the flat list (including child nodes)
# print("\nFlat List including Child Nodes:")
#dll.print_flat_list()




