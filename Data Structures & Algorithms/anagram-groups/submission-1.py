class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for w in strs:
            key = ''.join(sorted(w))
            groups.setdefault(key, []).append(w)
        return list(groups.values())










'''
understand:
first count loop through all the strings in array
then whichever has count equal, group that into a list

match- Array count problem

plan
def groupanagram:
    def count(word):
        count = {}
        for c in word:
            count[c]=count.get(c,0)+1
            return counts
    for w in str:
        count(w)
    
    group where counts are equal
    each group is a sublist
    return that sublist
        
'''