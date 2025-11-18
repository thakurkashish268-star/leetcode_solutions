class Solution(object):
    def maxDepth(self, root):
         if root==None:
             return 0
         lh =self.maxDepth(root.left)
         rh =self.maxDepth(root.right)
         return 1+max(lh,rh)