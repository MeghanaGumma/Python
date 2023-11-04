class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        osum=n*(n+1)//2
        asum=sum(nums)
        return (osum-asum)
        
