class Solution(object):
     def isBalanced(self, root):
          return self.dfheight(root)!=-1


     def dfheight(self,root):
         if root==None:
             return 0
        
         left=self.dfheight(root.left)
         if left==-1:
              return -1
        
         right=self.dfheight(root.right)
         if right==-1:
             return -1
        
         if abs(left-right)>1: 
             return -1
        
         return max(left,right)+1