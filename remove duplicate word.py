Remove duplicate word is one of medium coding challenge in LeetCode.

Basically, you just take one word and insert it in new variable, after you increment and the same word, it won't append

I consider on time and complexity to solve this coding challlenge down below
- Time complexity, I assign i as variable that will increment every word in one way. So time complexity will be O(n)
- Space complexity, I make new empty varible. Once I get word, it will insert it in new varibale. So space complexity will
be O(n)

Okey, lets code:

class solution():
    def remove_duplicate_word(self, word):
        s = word.split(' ')
        item = []
        for i in s:
            if i not in item:
                item.append(i)
        return (' '.join(item))
        
word = ('nama Ari nama Sulistiyo Prabowo')
solution().remove_duplicate_word(word)
