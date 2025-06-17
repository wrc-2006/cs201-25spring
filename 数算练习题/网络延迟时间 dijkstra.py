import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph={i:[] for i in range(1,n+1)}
        for i in times:
            graph[i[0]].append((i[1],i[2]))
        distance={i:float('inf') for i in range(1,n+1)}
        distance[k]=0
        p=[(0,k)]
        while p:
            time,node=heapq.heappop(p)
            if time>distance[node]:
                continue
            for v,w in graph[node]:
                if distance[v]>distance[node]+w:
                    distance[v]=distance[node]+w
                    heapq.heappush(p,(distance[v],v))
        ans=max(distance.values())
        if ans !=float('inf'):
            return ans
        return -1                    
    
if __name__=='__main__':
    sol=Solution()
    print(sol.networkDelayTime([[1,2,1]],2,1))
    