class Solution(object):
    
        def Inorder(self,root,result):
         
             if not root:
                 return
        
             self.Inorder(root.left,result)
             result.append(root.val)
             self.Inorder(root.right,result)
    
        def inorderTraversal(self, root):
             result=[]
             self.Inorder(root,result)
             return result