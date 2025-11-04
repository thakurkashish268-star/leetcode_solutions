class Solution(object):
    def twoSum(self, nums, target):
          
        mpp={}
        
        for i in range(len(nums)):
             more=target-nums[i]
        
             if more in mpp:                  
                  return[mpp[more],i]
                
             mpp[nums[i]]=i