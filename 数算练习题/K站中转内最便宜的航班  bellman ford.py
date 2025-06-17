class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        distance=[float('inf')]*n
        distance[src]=0
        for _ in range(k+1):
            cur=distance[:]
            for st,ed,cost in flights:
                if distance[st]+cost<distance[ed]:
                    cur[ed]=min(cur[ed],distance[st]+cost)
                    #min确保在本轮中多个航班可能更新同一个节点的问题。
                    #保护原来的cur值,如果有多个边可以到达ed，应该选最小的那个
            distance=cur
        if distance[dst]==float('inf'):
            return -1
        else:
            return distance[dst]
        
        
'''  #dijkstra 超时
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        pq=[(0,0,src)]  #cost,中转站,node
        dic=defaultdict(list)
        for i in flights:
            dic[i[0]].append((i[2],i[1]))   #cost,ed
        heapq.heapify(pq)
        while pq:
            cost,cnt,node=heapq.heappop(pq)
            if node==dst:
                return cost
            for i in dic[node]:
                need_cost,nextnode=i
                if cnt+1<=k or nextnode==dst:
                    heapq.heappush(pq,(cost+need_cost,cnt+1,nextnode))
        return -1
'''