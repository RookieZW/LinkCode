'''
翻转一个链表

样例
样例 1:

输入: 1->2->3->null
输出: 3->2->1->null
样例 2:

输入: 1->2->3->4->null
输出: 4->3->2->1->null
挑战
在原地一次翻转完成
'''
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        dummy = ListNode(None)
        while head:
           nxt = head.next
           head.next = dummy.next
           dummy.next = head
           head = nxt
        return dummy.next
'''
真神奇嘻嘻
'''