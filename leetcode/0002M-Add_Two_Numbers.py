# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_values = []
        l1_values.append(str(l1.val))
        while l1.next != None: 
            l1 = l1.next
            l1_values.append(str(l1.val))
        l2_values = []
        l2_values.append(str(l2.val))
        while l2.next != None: 
            l2 = l2.next
            l2_values.append(str(l2.val))
        l1_values.reverse()
        l2_values.reverse()
        l1_num = 0
        l2_num = 0
        if len(l1_values) >1: 
            l1_num = int("".join(l1_values))
        else: 
            l1_num = int(l1_values[0])
        if len(l2_values) > 1:
            l2_num = int("".join(l2_values))
        else: 
            l2_num = int(l2_values[0])
        res = l1_num+l2_num
        print(f"l1: {l1_num}, l2: {l2_num}")
        print(res)
        res = [int(n) for n in str(res)]
        start_node = None
        for i in range(len(res)): 
            new_node = ListNode(val = int(res[i]))
            new_node.next = start_node
            start_node = new_node
        if res == []: 
            start_node = ListNode()
        return start_node
        
        