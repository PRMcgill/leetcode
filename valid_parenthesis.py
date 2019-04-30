'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        s_dict = {'}':'{', ']':'[', ')':'('}
        for i in s:
            if i in s_dict.values():
                stack.append(i)
            elif i in s_dict.keys():
                if stack == []:
                    return False
                if s_dict.get(i) == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
        return stack == []