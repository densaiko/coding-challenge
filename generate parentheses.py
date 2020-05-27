Generate parentheses is a medium level coding challenge in Leetcode. In this coding challenge, I have to find how many
combinations of parentheses that are valid to be generated. 

For instance, I give 3 pairs of parentheses and I have to find the combination of that pairs. I solve this problem by giving
the open parentheses as a +1, once the next parentheses will give the open parentheses will be +1 and the close parentheses
will be -1. 

To solve this problem, I consider on the time and space complexity such as
- Time complexity will be O(n) because I use the brute force method but it's too complicated in math
- Space complexity will be O(n) because I need variable to keep the parentheses.

Lets code:

class solution():
    def generateparentheses(self, n):
        result = []
        
        def backtrack(a, left, right):
            if len(a) == 2*n:
                result.append(a)
                return
            if left < n:
                backtrack(a+'(', left+1, right)
            if left > right:
                backtrack(a+')', left, right+1)
        backtrack('', 0, 0)
        return result
        
solution().generateparentheses(3)
