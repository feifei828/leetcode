# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        i = head
        r = None
        if not i or not i.next:
            return head
        while i and i.next:
            temp = i.next
            i.next = temp.next
            temp.next = i
            if pre:
                pre.next = temp
            else:
                r = temp
            pre = i
            i = i.next
        return r
