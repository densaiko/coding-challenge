# First missing positive integer is one of the easy coding challenge in Leetcode, HackerRank and others.

# Here is the list of number [1, -2, 4, 2, 5, 7]

# You have to find the first missing positive integer in that list.

# The solution is so simple. I consider on the fastest solution based on time and space complexity:
# - Time complexity, I only use one variable to increment the integer. Once I got the first missing number, I stop incrementing
# - Space complexity, I don't new new list, dictionary or others to keep new integer

# Lets code:

class solution():
    def first_missing_positive_integer(self, nums):

        for i in range(1, len(nums)):
            if i not in nums:
                return i

nums = [1, -2, 4, 2, 5, 7]
print(solution().first_missing_positive_integer(nums))
