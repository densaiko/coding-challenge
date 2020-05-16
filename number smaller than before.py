number smaller than before is a unique coding challenge that I ever seen in Leetcode. As the name of number smaller than
before, I actually have to find how many number that I find during iteration from the initial number.

Here is the list of number [8, 1, 2, 2, 3]

For instance, '8' is the initial number and I have to find how many number that is small than my initial number, so in this 
case we know that there are four numbers that is smaller than '8'.

I consider on the time and space complexity:
- Time complexity, I use two variables, first variable will initialize the first number and second variable will increment
to find the smaller number than my initial number. So the time complexity will be O(n^2)
- Space complexity, I use new num to keep the how many numbers as I'm going to show this as a result. So the space complexity
will be O(n)

Lets code:

class solution():
    def number_smaller_than_before(self, nums):
        num = []
        for i in nums:
            a = 0
            for j in nums:
                if i > j:
                    a += 1
            num.append(a)
        return num    
        
nums = [8, 1, 2, 2, 3]
solution().number_smaller_than_before(nums)
