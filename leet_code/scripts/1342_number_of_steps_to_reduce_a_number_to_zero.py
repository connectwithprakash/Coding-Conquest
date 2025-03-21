"""
Input: Is a positive integer number
Output: Count that denotes the number of times we need to take to reduce it to zero following the rules
Idea: A simple approach would be to just add a bunch of conditional statement in a while loop until the value becomes zero 
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Using loop

        # num_steps = 0
        # while num:
        #     if num % 2 == 0:    # Is even
        #         num /= 2
        #     else:   # Is odd
        #         num -= 1
        #     num_steps += 1

        # return num_steps

        # Using recurrence
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps((num // 2))
        else:
            return 1 + self.numberOfSteps((num - 1))
