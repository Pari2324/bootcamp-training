# binary tree inorder traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def inorder(root):
            if root != None:
                inorder(root.left)  
                ans.append(root.val)     
                inorder(root.right)     
                     

        inorder(root)
        return ans
        