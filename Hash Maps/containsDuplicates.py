class Solution:
    def containsDuplicates(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
# Iterate through the entire array
# If n is in the hashset (duplicate) then return True denoting there are duplicates
# If not add n to the hashset and go to the next number and repeat

# O(n) time and space