'''
Two Sum
find the indexes of complimentary numbers
https://leetcode.com/problems/two-sum/submissions/
'''
#space efficient
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #loop through nums arr
        #for each number check to see if compliment exists in nums, not at same index
        copy = [*nums]
        index = 0;
        while len(copy) > 0:
            current = copy[0];
            diff = target-current;
            copy = copy [1:]
            
            if diff in copy:
                diff_index = copy.index(diff) + index + 1
                return [index, diff_index]
            index += 1 

#time efficient
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in nums_dict:
                nums_dict[diff] = i
            else:
                return [nums_dict[nums[i]], i]


'''
Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/submissions/
'''

class MyQueue:

    def __init__(self):
        self.size = 0
        self.stack_one = []
        self.stack_two = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.stack_two) > 0:
            curr = self.stack_two.pop()
            self.stack_one.append(curr)

        self.stack_one.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack_one) > 0:
            curr = self.stack_one.pop()
            self.stack_two.append(curr)
        return self.stack_two.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack_one) > 0:
            curr = self.stack_one.pop()
            self.stack_two.append(curr)

        return self.stack_two[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_one) == 0 and len(self.stack_two) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()