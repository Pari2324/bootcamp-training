# binary tree postorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(root):
            if root is None:
                return

            postorder(root.left)      # Left
            postorder(root.right)     # Right
            ans.append(root.val)      # Root

        postorder(root)
        return ans
        