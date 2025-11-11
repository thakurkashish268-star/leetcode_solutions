class Solution(object):
    def singleNumber(self, nums):
         xorr=0
         for i in range (len(nums)):
             xorr=xorr^nums[i]
         
         return xorr