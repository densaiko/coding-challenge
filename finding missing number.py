# Finding missing number is one of coding challenge in codewars. According to me, it's a easy coding challenge because 
# you have to use your understanding in algorithm to solve the problem

# Considering on time and space complexity, both of them is O(1).

# Lets code:

class solution():
    def find_missing_number(self, nums):
        return sorted(set(range(min(nums), max(nums)+1)).difference(nums))
        
        
nums = [-3, 1, 3, 6]
solution().find_missing_number(nums)
