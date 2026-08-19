class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            else:
                seen[n] = i



'''
Understand - 
nums = 
target = 
return i, j s.t
numi + numj = target

Match - I feel like I could use the 2 pointer thing here but not sure

Plan - 
calculate sums of all pairs in nums
compare sum with target
if there is a match
return the indices that led to the sum

Implement - 
def twoSum:
    def sum(num):
        for each i != j in num:
            sum = num[i]+num[j]
        return sum
    if sum(num) == target:
        return i, j    
'''
