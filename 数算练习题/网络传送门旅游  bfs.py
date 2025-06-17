from collections import defaultdict,deque
class Solution(object):
    def minMoves(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        n=len(matrix)
        m=len(matrix[0])
        door=defaultdict(list)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] not in '.#':
                    door[matrix[i][j]].append((i,j))
        #print(door)
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(x,y):
            visited={(x,y)}
            pq=deque([(0,x,y)])  #step,x,y
            while pq:
                step,x,y=pq.popleft()
                if x==n-1 and y==m-1:
                    return step
                if matrix[x][y] in door and matrix[x][y] not in visited:
                    for nx,ny in door[matrix[x][y]]:
                        if (nx,ny)!=(x,y):
                            pq.appendleft((step,nx,ny))
                    visited.add(matrix[x][y])
                for a,b in d:
                    nx,ny=x+a,y+b
                    if 0<=nx<n and 0<=ny<m:
                        if matrix[nx][ny]!='#' and (nx,ny) not in visited:
                            visited.add((nx,ny))
                            pq.append((step+1,nx,ny))
            return -1
        return bfs(0,0)
    
if __name__=='__main__':
    sol=Solution()
    print(sol.minMoves(["..C.","C.A."]))