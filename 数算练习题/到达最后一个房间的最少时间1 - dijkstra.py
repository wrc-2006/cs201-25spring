import heapq
class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        p=[]
        heapq.heappush(p,(0,0,0)) #time,x,y
        visited=set([(0,0)])
        n,m=len(moveTime),len(moveTime[0])
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        while p:
            time,x,y=heapq.heappop(p)   
            mintime=float('inf')    
            for a,b in d:
                nx,ny=x+a,y+b
                if nx==n-1 and ny==m-1 and time+1>moveTime[n-1][m-1]:
                    return time+1
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited:
                    if time+1>moveTime[nx][ny]:
                        visited.add((nx,ny))                 
                        heapq.heappush(p,(time+1,nx,ny))
                    else:
                        mintime=min(mintime,moveTime[nx][ny])
            heapq.heappush(p,(mintime,x,y))
        
        
if __name__=='__main__':
    sol=Solution()
    print(sol.minTimeToReach([[56,93],[3,38]]))