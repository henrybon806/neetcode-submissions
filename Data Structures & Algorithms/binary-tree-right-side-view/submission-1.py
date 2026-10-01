# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        output = []
        while queue:
            size = len(queue)
            idx = size - 1
            while queue[idx] is None:
                idx -= 1
                if idx <0:
                    break
            if idx >=0:
                output.append(queue[idx].val)
            for i in range(size):
                curr = queue.pop(0)
                if curr is not None:
                    queue.append(curr.left)
                    queue.append(curr.right)
        return output

