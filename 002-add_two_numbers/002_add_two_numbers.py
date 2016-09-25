# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        L = []
        node = self
        if node.val == 0 and node.next == None:
            return L.__str__()
        while node != None:
            L.append(node.val)
            node = node.next

        return L.__str__()


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)

        return dummyHead.next


def init_listnote(s):
    dummyHead = ListNode(0)
    LN = dummyHead
    for i in range(len(s)):
        LN.val = s[i]
        if i != len(s) - 1:
            LN.next = ListNode(0)
            LN = LN.next

    return dummyHead


if __name__ == '__main__':
    s1 = [3, 4, 2]
    s2 = [4, 6, 5]

    L1 = init_listnote(s1)
    L2 = init_listnote(s2)
    s = Solution()
    L3 = s.addTwoNumbers(L1, L2)
    print('input 1:', L1)
    print('input 2:', L2)
    print('output :', L3)
