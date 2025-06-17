def dfs(x,y,board,word,d,m,n,visited):
    if word=='':
        return True
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<m and 0<=ny<n:
            if board[nx][ny]==word[0] and visited[nx][ny]:
                visited[nx][ny]=False
                if dfs(nx,ny,board,word[1:],d,m,n,visited):
                    return True
                visited[nx][ny]=True
    return False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited=[[True]*n for _ in range(m)]
                    visited[i][j]=False
                    if dfs(i,j,board,word[1:],d,m,n,visited):
                        return True
        return False
        
if __name__ =='__main__':
    sol=Solution()
    print(sol.exist([["a","a"]],"aaa"))