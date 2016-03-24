def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root: return 0
    stack, level = [root], 1

    while stack:
        curr_num_nodes = len(stack)
        next_nodes = []
        while curr_num_nodes > 0
            curr_num_nodes -= 1
            node = stack.pop()
            if node.left: next_nodes.append(node.left)
            if node.right: next_nodes.append(node.right)
        if next_nodes:
            level += 1
        stack = next_nodes
    return level
