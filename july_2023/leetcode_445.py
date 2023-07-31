'''
level=medium
topic: stacks , linked list
logic: we are asked to add 2 numbers represented as linked list without reversing the linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack=[]
        l2_stack=[]
        ans=[]
        
        l1_pointer=l1
        while l1 and l1_pointer:
            l1_stack.append(l1_pointer)
            l1_pointer=l1_pointer.next

        l2_pointer=l2 
        while l2 and l2_pointer:
            l2_stack.append(l2_pointer)
            l2_pointer=l2_pointer.next 

        carry=0
        while l1_stack or l2_stack:
            temp=0
            if l1_stack:
                temp+=l1_stack.pop().val
            if l2_stack:
                temp+=l2_stack.pop().val 
            temp+=carry 
            new_val=temp%10 
            carry=temp//10 
            ans.append(ListNode(new_val))
        if carry:
            ans.append(ListNode(carry))

        for i in range(len(ans)-1, 0,-1):
            ans[i].next = ans[i-1]

        return ans[-1]
        


