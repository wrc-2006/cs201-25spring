class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=''
        minlen=len(strs[0])
        for i in strs[1:]:
            minlen=min(minlen,len(i))
        for i in range(minlen):
            st=strs[0][i]
            for j in strs[1:]:
                if j[i]!=st:
                    break
            else:
                ans+=st
                continue
            break
        return ans
    
            