# Queue reconstruction by height is really interesting challenge. In this challenge, you have to find how many people is taller
# than you in front of you. Each person is describe by a pair of integer (h, k), where h is the height and k is the number of
# people in front of this person who have a height greater than h or equal to h.

# Input : [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

# output : [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

# I consider on time and space complexity to solve this challenge
# - Time complexity, I will sort the input based on the tallest first, so it will be O(nlogn). After sorting, I will arange the
# output based on the smallest number of people and insert the pairs through iteration, so it will be O(n) * O(n) or O(n^2).
# Because O(n^2) is larger than O(nlogn), so the time complexity will be O(n^2).
# - Space complexity, I create new variable to keep the output into it, so the space complexity will be O(n).

# Lets code:

class Solution():
    def reconstructQueue(self, people):
        """Arrange the taller people to shorter people and calculate how many people that is taller
        in front of them"""
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []

        for p in people:
            result.insert(p[1], p)
        return result


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people))

