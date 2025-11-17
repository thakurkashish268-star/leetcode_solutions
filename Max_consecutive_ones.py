class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
         maxi=0
         cnt=0
         n=len(nums)
         for i in range(n):
             if nums[i]==1:
                 cnt+=1
                 maxi=max(maxi,cnt)
             else:
                 cnt=0
         return maxi