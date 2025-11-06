class Solution(object):
    def mySqrt(self, x):
         low=1
         high =x
         while low<=high:
             mid=low+(high-low)//2
             val=mid*mid
             if val<=x:
                 low=mid+1      
             else:
                 high=mid-1
         return high