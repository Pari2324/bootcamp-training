#minimum depth of binary tree
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return min( 1 + (self.minDepth(root.left)), 1 + (self.minDepth(root.right)))
        