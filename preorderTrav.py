def preorderTraversal(self, root):
    if root == None:
        return []
    def preord(root):
        if not root.left and not root.right:
            return [root.val]
        left = preord(root.left) if root.left else []
        right = preord(root.right) if root.right else []
        return [root.val] + left + right
  
    return preord(root)
