import sys
sys.setrecursionlimit(1<<30)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        arr=[]
        def dfs(record,position):
            if len(record)==n:
                #print(record)
                arr.append(record)
                return 
            lenth=len(record)
            for i in range(n):
                newrecord,newposition=record[:],position[:]
                newrecord.append('.'*i+'Q'+'.'*(n-1-i))
                newposition.append([lenth,i])
                for j in newposition[:-1]:
                    if j[1]==i or abs(j[0]-lenth)==abs(j[1]-i):
                        break
                else:
                    dfs(newrecord,newposition)
        dfs([],[])
        return arr

if __name__=='__main__':
    sol=Solution()
    print(sol.solveNQueens(4))