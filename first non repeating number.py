# First non repeating number coding challenge is the easiest challenge in LeetCode (Correct me if I wrong)

# To solve this coding challenge you can make it with time complexity O(n) and space complexity O(1)

# Okey, lets start coding

class solution():
    def first_non_repeating(self, x, n):
        for i in range(n):
            j=0
            while j<n:
                if i!=j and x[i] == x[j]:
                    break
                j+=1
            if j==n:
                return x[i]
        return 'a'
    
x = [9, 4, 9, 6, 7, 4]
n = len(x)
solution().first_non_repeating(x, n)
