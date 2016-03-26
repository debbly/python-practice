def isSymmetric(self, root):
    def check(r, l):
        if (r is None) != (l is None) : return False
        if r is None: return True
        if r.val != l.val: return False
        return check(r.left, l.right) and check(r.right, l.left)
    if root is None: return True
    return check(root.left, root.right)
