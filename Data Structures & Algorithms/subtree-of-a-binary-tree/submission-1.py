# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        if not subRoot:
            return True

        def dfs(root):
            nonlocal ans
            if not root or ans:
                return 

            if root.val == subRoot.val:
                ans = ans or self.isSameTree(root, subRoot)
                if ans:
                    return 

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ans
    
    def isSameTree(self, p, q):
        if (not p and q) or (p and not q):
            return False
        
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False