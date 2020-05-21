# Meeting rooms is a coding challenge from Facebook and it is a medium level based on Leetcode. In this coding challenge, 
# we have to find how many rooms that can provide meetings in a day. 

# For instance we have meeting at [7, 10], [8, 11], [13, 15]. So the there will be list inside list 
# [[7,10],[8,11],[13,15]]

# I consider on time and space complexity to answer this challenge.
# - Time complexity, I'm going to order and sort the list, so it will be O(nlogn) and I just pass through all value, so it will
# be O(n). Because O(nlogn) is bigger than O(n), so the time complexity will be O(nlogn)
# - Space complexity, I'm going to separate into different array, start and end meeting, so it will be O(n)

Lets code:
class solution():
    def meeting_room(self, intervals):
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
            
        s = 0
        e = 0
        available = 0
        numrooms = 0
        
        while s < len(start):
            
            if start[s] < end[e]:
                if available:
                    available -= 1
                else:
                    numrooms += 1
                s += 1
            else:
                available += 1
                e += 1
        return numrooms
            
intervals = [[0, 30], [5, 10], [15,20]]
print(solution().meeting_room(intervals))
