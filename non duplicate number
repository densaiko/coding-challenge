This coding challenge specifically for non duplicate number.

You have to find what number that has not been duplicated. The number is shown [4, 4, 3, 2, 2, 3, 1].

If you analyze the number, you focus on the word of 'duplicate' which means this list doesn't have more than two same number.

You can simply answer this with 
1. Time complexity with O(n^2) and space complexity with O(1)
2. Time complexity with O(n) and space complexity with O(1)

Luckily, I'm going to answer this challenge with second solution. I will consider on the method of XOR


class dup_solution():
    def dup_sol(self, nums):
        unique = 0
        for num in nums:
            unique ^= num
        return unique

nums = [4, 4, 3, 2, 2, 3, 1]    
dup_solution().dup_sol(nums)
