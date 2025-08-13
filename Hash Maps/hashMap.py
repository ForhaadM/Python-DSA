names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names: 
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1

print(countMap)

# Runs in O(n) time
# Insertion, Delection, and Search: O(1)