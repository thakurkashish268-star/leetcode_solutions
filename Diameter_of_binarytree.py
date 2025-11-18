class Solution(object):
     def diameterOfBinaryTree(self, root):
         self.diameter=0
         self.height(root)
         return self.diameter
     def height(self,root):
         if root==None:
             return 0
         lh =self.height(root.left)
         rh =self.height(root.right)
         self.diameter=max(self.diameter,lh+rh)
         return 1+max(lh,rh)