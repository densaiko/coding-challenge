# Permutation is one of coding challenge in Leetcode. In this coding challenge, we have to find the all possible permutations
# from the list given number. You can use the recursion method to answer the challenge

# Time complexity will how many combinations number (N), so the time complexity will be N factorial.
# Space complexity also will save how many combinations number (N), so the space complexity will be N factorial.

# Lets code:

class solution():
    def permute(self, nums):
        res = []
        
        def permutehelper(start):
            if start == len(nums)-1:
                res.append(nums[:])
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                permutehelper(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
                
        permutehelper(0)
        return res
    
nums = [1,2,3]
print(solution().permute(nums))
