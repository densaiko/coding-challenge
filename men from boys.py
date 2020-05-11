# Men from boys is not a game but it's one of coding challenge in medium level according to the Codewars platform. 

# Here is the rules:
# - Men should be an even number and ascending
# - Boys should be an odd number and descending

# The number is arranged in list [20, 33, 50, 34, 43, 46]

# To solve this coding challenge. I will consider on the time and space complexity:
# - Time complexity, I have to increment all the number in a list once. So time complexity will be O(n)
# - Space complexity, I have to make new varibale boys and men to keep the number based on even and odd number. So space 
# complexity will be O(n)

# Lets code:
class solution():
    def men_from_boys(self, arr):
        boys = []
        men = []
        for i in sorted(arr):
            if i % 2 == 0:
                men.append(i)
            else:
                boys.append(i)

        return men[::1] + boys[::-1]


arr = [20, 33, 50, 34, 43, 46]
print(solution().men_from_boys(arr))
