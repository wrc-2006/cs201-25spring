'''
def is_prime(n):
    lst=[True]*(n+1)
    primes=[]
    lst[1]=False
    for i in range(2,n+1):
        if lst[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            lst[i*p]=False
            if i%p==0:
                break
    return lst

class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=is_prime(100001)
        n=len(s)
        primes=[]
        for i in range(n):
            for j in range(i+1,n+1):
                if lst[int(s[i:j])]:
                    if int(s[i:j]) not in primes:
                        primes.append(int(s[i:j]))
        if lst[int(s[-1])] and int(s[-1]) not in primes:
            primes.append(int(s[-1]))
        primes.sort(reverse=True)
        ans=0
        for i in range(min(3,len(primes))):
            ans+=primes[i]
        return ans
        
滑动窗口
'''
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        primes=set()
        for left in range(len(s)):
            num=int(s[left])
            if is_prime(num):
                primes.add(num)
            for right in range(left+1,len(s)):
                num=int(s[left:right+1])
                if is_prime(num):
                    primes.add(num)
        primes=list(primes)
        primes.sort(reverse=True)
        return sum(primes[:3])