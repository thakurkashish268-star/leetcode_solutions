class Solution(object):
    def maxProduct(self, nums):
         n= len(nums)
         pre=1
         suff=1
         ans=nums[0]
         for i in range (len(nums)):
             if(pre==0):
                 pre=1
             if(suff==0):
                 suff=1

             pre=pre * nums[i]
             suff=suff * nums[n-1-i]
             ans =max(ans,pre,suff)
      
         return ans