'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#   def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        l3 = current = ListNode(0)
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            elif l1 is not None:
                current.next = l1
                break
            else:
                current.next = l2
                break

        return l3.next


if __name__ == '__main__':
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(4)

    L2 = ListNode(1)
    L2.next = ListNode(3)
    L2.next.next = ListNode(4)

    s = Solution()
    L3 = s.mergeTwoLists(L1, L2)
    while L3 is not None:
        print(L3.val)
        L3 = L3.next






        