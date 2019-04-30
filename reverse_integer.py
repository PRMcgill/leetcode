'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)[::-1]
        if '-' in x:
            x = x[:-1]
            if int('-' +x) < - (2 **31 -1):
                return 0
            return int('-' +x)
        else:
            if int(x) > 2 ** 31 -1:
                return 0
            return int(x)