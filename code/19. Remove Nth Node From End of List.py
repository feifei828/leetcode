class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = None
        i = head
        j = head
        while n > 0:
            j = j.next
            n -= 1
        while j:
            pre = i
            i = i.next
            j = j.next
        if pre is None:
            return i.next
        pre.next = i.next
        return head
