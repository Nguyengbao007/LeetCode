# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#solution1
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=sorted(s)
        t=sorted(t)
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            if s[i]!=t[i]:
                return False
            else:
                return True
print(Solution1().isAnagram("anagram","nagaram"))
#solution2
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_s_list=list(s)
        char_t_list=list(t)
        fre=[0]*25
        for i in range(0,26):
            k=(char_s_list[i])-97
            fre[k]+=1
        for i in range(0,26):
            k=int(char_t_list(i))-97
            if fre[k]==0:
                return False
            fre[k]-=1
        return True
print(Solution2().isAnagram("anagram","nagaram"))