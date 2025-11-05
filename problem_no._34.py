class Solution(object):
     def lower(self, nums,n,x):
         low =0 
         high=n-1 
         ans =n
         while low<=high:
             mid=(low + high)//2
             if nums[mid]>=x:
                 ans=mid
                 high= mid-1
             else:
                 low=mid+1
         return ans


     def upper(self, nums,n,x):
    
         low =0 
         high=n-1
         ans =n
         while low<=high:
             mid=(low + high)//2
             if nums[mid]>x:
                 ans=mid
                 high= mid-1
             else:
                 low=mid+1
         return ans

     def searchRange(self, nums, target):
         n= len(nums)  
         lb=self.lower(nums,n,target)
         if lb==n or nums[lb]!=target:
             return [-1,-1]
         return [lb,self.upper(nums,n,target)-1]
    
        