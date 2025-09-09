class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to List of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c)- ord("a")] += 1 # ord gives the ASCII value
            res[tuple(count)].append(s)

        return list(res.values())

        # Runtime: O(m * n)

        