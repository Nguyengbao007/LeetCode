# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
a=[8,3,8,2]
first=-1
second=-1
third=-1
for i in range(0,len(a)):
    num=a[i]
    if a[i]==first or a[i]==second or a[i]==third:
        continue
    if first==-1 or num>first:
        third=second
        second=first
        first=num
    elif second==-1 or num>second:
        third=second
        second=num
    elif third==-1 or num>third:
        third=num
if third==-1:
    third=first
print(third)