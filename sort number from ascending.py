# sort number from ascending is the simple coding challenge. However, it will be useful to sort the number to get
# the structured data

# This solution is a solution that you pretend to code. But no problem about that, lets we pretend to code :)

# OR, if you think you don't need to pretend, you can simply use the 'sorted' function to sort number from ascending :(
    
# I pretend to code :)
    
# I consider time and space complexity down below:
# - Time complexity O(n) because I only use one variable i to loop the entire number in list
# - Space complexity O(1) because I don't need an empty list to keep the number

# Lets find the solution

class solution():
    def sort_num_ascending(self, nums):
        nums_one = 0
        nums_two = 0
        nums_three = 0
        for n in nums:
            if n == 1:
                nums_one = 1 + nums_one
            elif n == 2:
                nums_two = 1 + nums_two
            elif n == 3:
                nums_three = 1 + nums_three
                
        return [1]*nums_one + [2]*nums_two + [3]*nums_three
        
nums = [3, 3, 2, 1, 3, 2, 1]
solution().sort_num_ascending(nums)
