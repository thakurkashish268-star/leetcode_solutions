class Solution(object):
   def fourSum(self, nums, target):
     ans=[]

    #sort the given array:
     nums.sort()
     n=len(nums)
    #calculating the quadruplets:
     for i in range(n-3): 
        # avoid the duplicates while moving i:
        if i > 0 and nums[i] == nums[i - 1]:
           continue
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
        for j in range(i+1, n-2):
            #avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
              continue
            # Early pruning for j
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                 sum = nums[i]+nums[j]+nums[k]+ nums[l]
                 if sum == target:
                     ans.append([nums[i], nums[j], nums[k], nums[l]])
                     k+=1 
                     l-=1
                     #skip the duplicates:
                     while k < l and nums[k] == nums[k - 1]:
                        k+=1
                     while k < l and nums[l] == nums[l + 1]:
                        l-=1
                 elif sum < target: 
                     k+=1
                 else:
                     l-=1 
     return ans
