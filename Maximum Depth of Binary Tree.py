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


def maxDepth(root,count=0):
    """
    :type root: TreeNode
    :rtype: int
    """
    node=root
    if node is None:
        return count
    count+=1
    return max(maxDepth(node.left,count),maxDepth(node.right,count))


# Example usage
bt = BinaryTree()
values = [10, 6, 15, 3, 8, 12, 17]

for value in values:
    bt.insert(value)

# print("In-order traversal:")
# bt.inorder_traversal(bt.root)
# print("\nPre-order traversal:")
# bt.preorder_traversal(bt.root)
# print("\nPost-order traversal:")
# bt.postorder_traversal(bt.root)

print(maxDepth(bt.return_root()))





    