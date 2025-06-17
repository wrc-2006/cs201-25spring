import sys
sys.setrecursionlimit(1<<30)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=set()
        record=[0]*len(digits)
        def backtrack(record):
            string=''
            for i in range(len(digits)):
                if record[i]<len(dic[digits[i]]):
                    string+=dic[digits[i]][record[i]]
            if string:
                ans.add(string)
            for i in range(len(digits)):
                if record[i]<len(dic[digits[i]])-1:
                    newre=record[:]
                    newre[i]+=1
                    backtrack(newre)
        backtrack(record)
        return list(ans)
    
if __name__=='__main__':
    sol=Solution()
    print(sol.letterCombinations('22'))