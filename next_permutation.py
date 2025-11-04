class Solution(object):
    def nextPermutation(self, nums):
         n=len(nums)
         ind=-1 
         for i in range(n-2,-1,-1):
             if nums[i]<nums[i+1]:
                 ind=i
                 break
        
         if ind==-1:
             nums.reverse()
             return
        
         for i in range(n-1,ind,-1):
             if nums[i]>nums[ind]:
                 t=nums[i]
                 nums[i]=nums[ind]
                 nums[ind]=t
                 break
               
         nums[ind+1:]=reversed(nums[ind+1:])