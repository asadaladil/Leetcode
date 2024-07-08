class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
    
    def return_root(self):
        return self.root

    def _insert(self, current, key):
        # This example method will insert nodes in level order for simplicity
        queue = [current]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(key)
                break
            else:
                queue.append(node.left)
            if not node.right:
                node.right = TreeNode(key)
                break
            else:
                queue.append(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=" ")

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root==None:
        return []
    arr=[]
    Queue=[root]
    value=0
    aa=0
    temp=[]
    while Queue:
        if value==0:
            aa=len(Queue) # level onujai packet korar jonno 67 and 71 line likha hoeche, jokhn ektao pop kora hoini
        node=Queue[0]
        Queue=Queue[1:]
        value+=1
        temp.append(node.val)
        if node.left:
            Queue.append(node.left)
        if node.right:
            Queue.append(node.right)
        if aa==value:
            arr.append(temp)
            temp=[]
            value=0
    return arr
            


# Example usage
bt = BinaryTree()
values = [10, 6, 15, 3, 8, 12, 17]

for value in values:
    bt.insert(value)

print(levelOrder(bt.return_root()))





    