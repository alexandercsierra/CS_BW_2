'''
Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        #account for edge cases where one list is empty
        if l2 is None and l1 is not None:
            return l1
        elif l1 is None and l2 is not None:
            return l2


        #this will hold a list of all the nodes in the order they appear in each list, l1 followed by l2
        node_list = []
        #will hold a list of tuples. the first value will be the node's value, the second will be its index in the node list array
        node_tuples = []

        #initializing more legible variables
        node_one = l1
        node_two = l2
        #start a counter to keep track of index
        counter = 0

        #traverse list 1 adding nodes to the node list and appropriate tuples to the node_tuples list
        while node_one is not None:
            node_list.append(node_one)
            node_tuples.append((node_one.val, counter))
            node_one = node_one.next
            counter+=1

        #same for list 2
        while node_two is not None:
            node_list.append(node_two)
            node_tuples.append((node_two.val, counter))
            node_two = node_two.next
            counter+=1

        #sort the tuples by node value
        node_tuples.sort(key=lambda tup: tup[0])

        #initialize a final ordered list of all the nodes
        final_node_list = []

        #loop through the tuples list adding nodes to the final list and appropriately chaining them together
        for i in range(len(node_tuples)-1):
            current_node = node_list[node_tuples[i][1]]
            next_node = node_list[node_tuples[i+1][1]]
            final_node_list.append(current_node)
            current_node.next = next_node

        #assuming both lists aren't empty, return the first node in the final list
        if len(final_node_list) > 0:
            return final_node_list[0]


class Solution:
    def decodeString(self, s: str) -> str:
        #convert the string to a list of characters
        chars = list(s)
        stack = []
        openers = []

        for i in range(len(chars)):
            stack.append(chars[i])

            if chars[i] == '[':
                openers.append(i)
            if chars[i] == ']':
                substring = ""
                closing = stack.pop()
                while len(stack) > openers[-1] + 1:
                    substring = stack.pop() + substring
                #opening bracket
                stack.pop()
                openers.pop()
                multiplier = stack[-1]
                substring = int(multiplier) * substring
                sub_list = list(substring)
                stack = [*stack, *sub_list]

        print(stack)

