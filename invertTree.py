def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(roo.right)
    return root
