class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for _ in nums:
            total += self.prefix.append(total)
    
    def rangeSum(self,left,right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1 ] if left > 0 else 0
        return (preRight - preLeft)
