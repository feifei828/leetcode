# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = self.getval(l1)
        l2_num = self.getval(l2)
        l3_num = l1_num + l2_num

        l3 = ListNode(l3_num % 10)
        head = l3
        index = 1
        while l3_num / (10 ** index):
            l = ListNode((l3_num / (10 ** index)) % 10)
            head.next = l
            head = l
            index += 1

        return l3

    def getval(self, l):
        num = 0
        index = 0
        while l:
            num += l.val * (10 ** index)
            l = l.next
            index += 1
        return num