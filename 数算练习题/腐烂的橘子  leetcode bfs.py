from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bad=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    bad.append([i,j])
        inq=set()
        q=deque()
        for i,j in bad:
            q.append((i,j,0))
            inq.add((i,j))
        d=[(0,1),(1,0),(0,-1),(-1,0)]
        for i in grid:
            if 1 in i:
                break
        else:
            return 0
        while q:
            x,y,time=q.popleft()
            for a,b in d:
                nx,ny=x+a,y+b
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]):
                    if grid[nx][ny]==1 and (nx,ny) not in inq:
                        q.append((nx,ny,time+1))
                        inq.add((nx,ny))
                        grid[nx][ny]=2
            print(grid)
            for i in grid:
                if 1 in i:
                    break
            else:
                return time+1
        return -1
                        
if __name__ =='__main__':
    sol=Solution()
    print(sol.orangesRotting([[0,2]]))