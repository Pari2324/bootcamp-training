#Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalcolor=image[sr][sc]
        if originalcolor==color:
            return image
        rows,cols=len(image),len(image[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=originalcolor:
                return
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image