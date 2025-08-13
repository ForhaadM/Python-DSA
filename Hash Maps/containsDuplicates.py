class Solution:
    def containsDuplicates(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums: # here n is the value NOT the index of the value
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
# Iterate through the entire array
# If n is in the hashset (duplicate) then return True denoting there are duplicates
# If not add n to the hashset and go to the next number and repeat

# O(n) time and space
#adding comment for intial commit
