# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return 'None'
        self.preorder = []
        def preorder(root):
            if root is None:
                self.preorder.append(None)
                return
            self.preorder.append(root.val)
            preorder(root.left)     
            preorder(root.right)

        preorder(root)
        return str(self.preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'None':
            return None
        data = data[1:-1].split(',')
        preorder = [int(x) if x != " None" else None for x in data]

        self.idx = 0
        def findTree():
            if self.idx >= len(preorder):
                return
            val = preorder[self.idx]
            self.idx += 1
            if val is None:
                return
            root = TreeNode(val=val)
            root.left = findTree()
            root.right = findTree()
            return root
        return findTree()
            


