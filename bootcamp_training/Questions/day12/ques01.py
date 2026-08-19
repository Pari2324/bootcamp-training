class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(9)
root.left.right.left = TreeNode(1)

print(root)