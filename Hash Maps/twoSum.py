class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # enumerate lets you loop through both the index and the value at the same time.
        for i, n in enumerate(nums): # i is the index of the current element in nums. # n is the value of the current element in nums. 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i