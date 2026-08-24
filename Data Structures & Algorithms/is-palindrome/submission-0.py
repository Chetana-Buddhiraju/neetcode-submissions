class Solution:
    def isPalindrome(self, s: str) -> bool:
        def cleaned(word):
            result = ""
            for l in word:
                if l.isalnum():
                    result += l.lower()
            return result

        w = cleaned(s)
        if w == w[::-1]:
            return True
        else:
            return False





'''
u- you need to read the thing from front and back
store the front first reading order in one array and the back first reading order in another array
compare the 2 arrays 
if they are equal - return true 
else - false

m- two pointer something no

p- 
read from front and save the string - for l in s: add l to m
read from back and save the string - for -l in s: add -l to n
if m == n: return true
else return false
'''
        