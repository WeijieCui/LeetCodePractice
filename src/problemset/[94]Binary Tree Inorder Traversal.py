# Given the root of a binary tree, return the inorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 13301 👎 759
# leetcode submit region begin(Prohibit modification and deletion)
import queue
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            values.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        return values

# leetcode submit region end(Prohibit modification and deletion)
