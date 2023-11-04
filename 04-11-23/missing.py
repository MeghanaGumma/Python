#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
class Solution:
    def missingNumber(self,array,n):
        osum=n*(n+1)//2
        asum=sum(array)
        return (osum-asum)
