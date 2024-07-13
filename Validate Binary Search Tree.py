
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

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


def isValidBST(root): # memory save kore kintu time beshi ney
    if root is None:
        return True
    def DFS(node,min,max):
        if node.val<=min or node.val>=max:
            return False
        if node.left:
            if not DFS(node.left,min,node.val):
                return False
        if node.right:
            if not DFS(node.right,node.val,max):
                return False
        return True
    return DFS(root,-1e18,1e18)


def isValidBST2(root): #memory beshi lagleo time kom ney
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    res=[]
    arr=[]
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            arr.append(node.val)
            inorder_traversal(node.right)
    inorder_traversal(root)
    res=arr
    res.sort()
    return res==arr and len(arr)==len(set(arr)) # same number jodi thake tahole seta bst hobe na


bst = BinarySearchTree()
values = []

for value in values:
    bst.insert(value)

print(isValidBST2(bst.root))

# print("In-order traversal of the BST:")
# bst.inorder_traversal(bst.root)