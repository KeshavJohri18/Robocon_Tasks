# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if(list1 is None and list2 is None):
            return list1
        
        if(list1 is None and list2 is not None):
            return list2
        
        if(list2 is None and list1 is not None):
            return list1

        
        head = list1
        array = []

        while(head is  not None):
            array.append(head.val)
            head = head.next
        
        head = list2

        while(head is  not None):
            array.append(head.val)
            head = head.next
        
        array.sort(reverse = False)

        join = list1
    
        while(join.next is  not None):
            join = join.next
        
        join.next = list2
        temp = list1
        i = 0

        while(temp is  not None):
            temp.val = array[i]
            temp = temp.next
            i += 1    

        return list1