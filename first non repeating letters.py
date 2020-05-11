# First non repeating letters is a coding challenge that I have when I faced an coding interview from one of multinational
# company from Sweden. This coding interview is a medium coding challenge from me because I failed my first try and pass it with
# two trials

# Here is the question
# You have a string like this 'sTreSS'. You have to find first non repeating letters which the answer have to match with the 
# original string. 

# I consider on time and space complexity to answer this question:
# 1. Time complexity, you have to increment the whole string once. So the time complexity is O(n)
# 2. Space complexity, you need another variable to keep the letter to find the first non repeating letter. So the space
# complexity will be O(n)

# Lets code:

class solution():
    def first_non_repeating_letters(self, string):
        low_string = []
        for i in string:
            low_string.append(i.lower())
        for i in string:
            if low_string.count(i.lower()) == 1:
                return i
        return ''


string = 'sTreSS'
print(solution().first_non_repeating_letters(string))
