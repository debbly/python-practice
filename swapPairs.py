def swapPairs(self, head):
    if not head or not head.next:
        return head

    first, second = head, head.next
    third = second.next
    head = second
    second.next = first
    first.next = self.swapPairs(third)

    return head
