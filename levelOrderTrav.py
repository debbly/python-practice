def levelOrderBottom(self, root):
    answ, listl = [], [root]
    while listl and root:
         answ.insert(0, [n.val for n in listl])
             listl = [ value for node in listl for value in (node.left, node.right) if value ]

    return answ
