class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        number_counter = collections.Counter(A)
        for i in number_counter:
            if number_counter[i]> 1:
                return i