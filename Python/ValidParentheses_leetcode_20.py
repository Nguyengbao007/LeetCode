# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type. 
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([])"
# Output: true

#Solution1:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.stack=[]
        for i in range(len(s)):
            if s[i]=="{" or "[" or "(":
                self.stack.append(s[i])
            else:
                if self.stack.clear():
                        return False
                if s[i]=="}":
                     if self.stack.pop() != "{":
                          return False
                if s[i]=="]":
                     if self.stack.pop() != "[":
                          return False
                if s[i]==")":
                     if self.stack.pop() != "()":
                          return False
print(Solution().isValid("(]"))                     