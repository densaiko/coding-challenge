# Top K Frequent Element is a medium coding challenge in Leetcode. This challenge can be solved using the Heap, once you get the 
# minimum number with the most frequency based on the number of K. 

# For instance, if the number of K is 2 and the numbers in list are [1,1,1,2,2,3], which means that you have to give the result
# number that has the 2 most frequency, and it is 1 and 2. 

# Lets code:

import heapq

class Solution:
  def topKFrequent(self, nums, k):
      count = collections.defaultdict(int)
      for n in nums:
          count[n] += 1
      heap = []
      for key, v in count.items():
          heapq.heappush(heap, (v, key))
          if len(heap) > k:
              heapq.heappop(heap)
      res = []
      while len(heap) > 0:
          res.append(heapq.heappop(heap)[1])
      return res

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
