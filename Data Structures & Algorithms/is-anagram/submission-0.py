class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def count(word):
            counts = {}
            for ch in word:
                counts[ch] = counts.get(ch, 0) + 1
            return counts

        m = count(s)
        n = count(t)
        return m == n

        












'''
UMPIRE - Understand Match Plan Implement Review Evaluate

U - I have to compare all the letters in string s with all the letters in string t, and if same I have to return true, else false. first I have to loop through each string to form arrays with individual letters in each string. After the 2 arrays are formed, we have to compare and see if array a == array b and if yes, true, else false.

M - Not sure what equal checking matches to. set hashing is what? and how many such methods or patterns are there that I need to learn and match to?

P - array a = [elements of letters from s]
array b = [element of letters from t]
for array a and array b:
    if array a == array b:
        return true
    return false

I - for l in s:
add l to a
for m in t:
    add m to b
if a == b:
    return true
return false
'''