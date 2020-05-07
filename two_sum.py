Two sum is a simple coding challenge that we have to find the two number in list which is the sum to get result that are
on the target.

The list contains [1, 8, 10, 15], and target is 18

There are two method to find the two number in a list to achieve the target
1. We can use two increment (i and j). every i in index, j will increment the rest until the two number match with the target.
I consider on the time complexity is O(n^2) and space complexity is O(1)

2. We can use one increment (i). Every i in index, the target will substract the number in each i and save it in dictionary.
I consider on the time complexity is O(n) and space complexity is O(n)

class solution():
    def two_sum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            if target-num in dict:
                return (dict[target-num], i)
            dict[num] = i
        return 'a'
    
nums = [1, 8, 10, 15]
target = 18

solution().two_sum(nums, target)
