Find two maximum number is one of the coding challenge in LeetCode. 

This coding challenge helps us to generate the maximum or even the minimum number that we want to retrieve

Basically, it's in easy coding challenge that you just use one variable (i) or two variables (i and j) to increment through
the list

There are two approachment to solve this challenge
1. You can use two variables (i and j), which i will lock one number and let j increment the rest. You may consider
time complexity will be O(n^2) because you will repeat the loop until you find the solution
space complexity will be O(n) because you will take one maximum number in your new empty list

2. You can use one varible (i), which i won't increment but only making the sum of maximum number of the question
time complexity will be O(n) because you will loop the two maximum to solve the challenge
space complexity will be O(n) because you will take on maxium number in your new empty list until you get two maximum number

Lets use the second solution to use the fastest solution

class solution():
    def find_two_maximum(self, ages):
        maximum = []
        for i in range(2):
            maximum.append(max(ages))
            ages.remove(max(ages))
        
        return sorted(maximum)

ages = [6, 5, 83, 5, 3, 18]
solution().find_two_maximum(ages)
