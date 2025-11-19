class Solution(object):
     def maxPathSum(self, root):
         self.maxx = float('-inf')
         self.maxPath(root)
         return self.maxx
    
     def maxPath(self,root ):
         if root is None:
             return 0
        
         left=max(0,self.maxPath(root.left))
         right=max(0,self.maxPath(root.right))
         self.maxx=max(self.maxx,left+right+root.val)
         return max(left,right)+root.val
    
        