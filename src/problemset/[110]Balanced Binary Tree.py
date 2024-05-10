# Given a binary tree, determine if it is height-balanced. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 10533 👎 667


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        nodes = [root]
        sub_nodes = []
        while True:
            print([node.val for node in nodes])
            for node in nodes:
                if node.left is not None:
                    sub_nodes.append(node.left)
                if node.right is not None:
                    sub_nodes.append(node.right)
            print([node.val for node in sub_nodes])
            if len(sub_nodes) < len(nodes) * 2:
                return not any(node.left is not None or node.right is not None for node in sub_nodes)
            nodes = sub_nodes
            sub_nodes = []
# leetcode submit region end(Prohibit modification and deletion)
