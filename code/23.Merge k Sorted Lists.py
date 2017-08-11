
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        walk_list = [lists[i] for i in range(len(lists))]
        pre = None
        while len(filter(lambda x: x is not None, walk_list)):
            for i in range(len(walk_list)):
                if walk_list[i] is not None:
                    min_val = walk_list[i].val
                    min_index = i
                    break
            for i in range(len(walk_list)):
                if walk_list[i] and walk_list[i].val < min_val:
                    min_val = walk_list[i].val
                    min_index = i
            l = ListNode(min_val)
            walk_list[min_index] = walk_list[min_index].next
            if head is None:
                head = l
                pre = head
            else:
                pre.next = l
                pre = l
        return head


class NewSolution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return None
        i = 0
        j = len(lists) - 1
        r_list = lists
        while i < j:
            l = []
            while i < j:
                node = self.mergetwolists(r_list[i], r_list[j])
                l.append(node)
                i += 1
                j -= 1
            if i == j:
                l.append(r_list[i])
            r_list = l
            i = 0
            j = len(r_list) - 1
        return r_list[0]

    def mergetwolists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        l1_head = l1
        l2_head = l2
        head = None
        pre = None
        while l1_head and l2_head:
            if l1_head.val < l2_head.val:
                l = ListNode(l1_head.val)
                l1_head = l1_head.next
            else:
                l = ListNode(l2_head.val)
                l2_head = l2_head.next

            if pre == None:
                pre = l
                head = l
            else:
                pre.next = l
                pre = l

            if l1_head is None:
                pre.next = l2_head
            if l2_head is None:
                pre.next = l1_head
        return head
