class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans=[]
        st,ed=intervals[0][0],intervals[0][1]
        for i in intervals[1:]:
            if i[0]<=ed:
                ed=max(ed,i[1])
            else:
                ans.append([st,ed])
                st,ed=i[0],i[1]
        ans.append([st,ed])
        return ans