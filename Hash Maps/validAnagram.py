class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for char in s:
            if char in hashMap1:
                hashMap1[char] += 1
            else:
                hashMap1[char] = 1
        for char in t:
            if char in hashMap2:
                hashMap2[char] += 1
            else:
                hashMap2[char] = 1
        
        if hashMap1 == hashMap2:
            return True
        else:
            return False
        
# Loop through both strings s and t
# If the char is in the hashMap increase its counter by 1 if not set the counter to 1
# Compare the counters of both hash maps. Return true if both counters are the same (i.e both s and t have the same letters and the same number of letters). Return false otherwise

# Runtime: O(n+m) where n = len(s) and m = len(t)
# Space: O(n) worst case if every character is unique. O(1) average

# More optimal Hash Map Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # return 0 is s[i] doesnt exist in counts
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# countS.get(s[i], 0)
# Checks if the character s[i] exists in the dictionary countS
# if it does, it returns the exisiting count
# if it does not, it returns 0 (default value passed to .get() )
# .get() retrives the value for a given key with a built in safety feature
# "Look up the current count for s[i] in countS. If it’s not there, just use 0."

# 1 + countS.get(s[i], 0)
# Takes the current count (or 0 if not found) and adds 1 - meaning we have seen this character one more time

# countS[s[i]] = ...
# Updates the dictionary countS so that the key s[i] has the new incremented count.

# Runtime: O(n+m) where n = len(s) and m = len(t)
# Space: O(1)

