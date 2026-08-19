# binary tree level order traversal
 if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans