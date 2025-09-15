# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 
# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.
from collections import deque
from queue import LifoQueue
#definition of stack
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
#way1
class Solution1(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)
        l=0
        r=n-1
        temp=0
        while l<r:
            temp=s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1
            r-=1
        return s
print('solution1 using two pointers')
print(Solution1().reverseString(["h","e","l","l","o"]))
#way2
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack=LifoQueue()
        for i in range(len(s)):
            stack.put(s[i])
        i=0
        while stack.empty()==False:
            s[i]=stack.get()
            i+=1
        return s
print('solution2 using stack')
print(Solution2().reverseString(["h","e","l","l","o"]))