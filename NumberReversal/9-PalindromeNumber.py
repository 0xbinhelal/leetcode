class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ox = x
        y = 0

        while x > 0:
            d = (x % 10)
            x = x // 10
            y = (y * 10) + d

        if ox == y:
            return True
        return False
