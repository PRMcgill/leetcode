'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

import copy
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        array=[]
        for i in range(len(A)):
            if(A[i]%2==0):
                array.append(A[i])
        temp=copy.deepcopy(array)
        for i in A:
            if(i not in temp):
                array.append(i)
        return array