def lowestCommonAncestor(self, root, p, q):
    if (p.val <= root.val <= q.val or q.val <= root.val <= p.val):
        return root.val
    if (p.val < root.val and q.val < root.val): return self.lowestCommonAncestor(root.left, p, q)
    if (p.val > root.val and q.val > root.val): return self.lowestCommonAncestor(root.right, p, q)
