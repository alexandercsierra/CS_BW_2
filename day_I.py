'''
Contains Duplicate
https://leetcode.com/submissions/detail/357073004/
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #define a dictionary that will store values we've seen
        counts = {}
        
        #iterate through list of numbers noting a count in the dictionary
        for num in nums:
            
            #if we've seen this number before, it's a duplicate
            if num in counts:
                #break out of the loop if there are any duplicates
                return True
            
            #if not, add it to dictionary
            counts[num] = 1
            
        #return false if no duplicates were found
        return False



'''
Add Two Numbers
https://leetcode.com/submissions/detail/357083805/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #use helper function to convert ll into a number
        num1 = self.ll_to_num(l1);
        num2 = self.ll_to_num(l2);
        
        
        # add two resulting numbers
        the_sum = num1 + num2
        
        #helper function creates linked list out of a number
        return self.num_to_ll(the_sum)
            
            
    def ll_to_num(self, head):
        #intialize total variable
        #initialize variable to hold decimal place
        total = 0;
        place = 1;
        
        curr = head
        
        #iterate through the list
        while curr is not None:
            
            #add value to total taking into account the decimal place
            total += curr.val * place
            
            #increment the dec place and current
            place *= 10
            curr = curr.next
            
        return total
    
    def num_to_ll(self, number):
        #split number into an array
        num_arr = [int(num) for num in str(number)]
        
        #initialize head of list
        head = ListNode(num_arr.pop())
        current = head
        
        #while length of array is not zero, pop off numbers
        while len(num_arr) > 0:
            
            #create a node for each number, linked together with previous node
            current.next = ListNode(num_arr.pop())
            current = current.next
            
        return head