# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, curr_min, curr_max = q.popleft()
            if node.val <= curr_min or node.val >= curr_max:
                return False

            if node.left:
                q.append((node.left, curr_min, min(curr_max, node.val)))
            if node.right:
                q.append((node.right, max(curr_min, node.val), curr_max))

        return True