def reverseList(self, head):
    if not head: return head
    p, q = head, head.next
    p.next = None

    while q:
        tmp, q.next = q.next, p
        p, q = q, tmp

    return p
