# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
'''

class Solution(object):
    def rangeSumBST(self, root, L, R, total=0):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root: return total
        
        total = self.rangeSumBST(root.left, L, R, total)
        if root.val >= L and root.val <= R:
            total += root.val
        total = self.rangeSumBST(root.right, L, R, total)
            
        return total