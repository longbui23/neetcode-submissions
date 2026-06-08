# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, float('-inf'))])
        count = 0

        while q:
            node, curr_max = q.popleft()
            if node.val >= curr_max:
                count += 1

            if node.left:
                q.append((node.left, max(node.val, curr_max)))
            if node.right:
                q.append((node.right, max(node.val, curr_max)))

        return count
