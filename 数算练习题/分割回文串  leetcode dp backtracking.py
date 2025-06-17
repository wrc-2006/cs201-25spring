class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n=len(s)
        ans=[]
        record=[[True]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]!=s[j] or record[i+1][j-1]==False:
                    record[i][j]=False
        arr=[]
        def dfs(i,arr):
            for j in range(i,n):
                if record[i][j]:
                    dfs(j+1,arr+[s[i:j+1]])
            if i==n:
                ans.append(arr)
        dfs(0,[])
        return ans
    
if __name__=='__main__':
    sol=Solution()
    print(sol.partition('aab'))