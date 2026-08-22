# minimum and maximum elements in a BST
def findMinMax(root):
    if root in None:
        return None, None
    minNode = root
    while minNode.left:
        minNode = minNode.left
    maxNode = root
    while maxNode.right:
        maxNode = maxNode.right
    return minNode.val, maxNode.val