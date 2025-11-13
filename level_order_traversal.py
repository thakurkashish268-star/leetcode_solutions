from collections import deque
class Solution(object):

     def levelOrder(self, root):
         ans = []
         if root is None:
             return ans

         q = deque()
         q.append(root)

         while q:
             size = len(q)
             level = []

             for i in range(size):
                 node = q.popleft()
                 if node.left:
                     q.append(node.left)
                 if node.right:
                     q.append(node.right)
                 level.append(node.val)
            
             ans.append(level)
        
         return ans
