#FIND if path exiists in graph 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n

        def dfs(node):
            if node == destination:
                return True

            visited[node] = True

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True

            return False

        return dfs(source)
