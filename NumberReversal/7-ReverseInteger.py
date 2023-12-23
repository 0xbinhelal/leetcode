# Without using strings
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = x * -1
            negative = True

        y = 0
        while x > 0:
            d = x % 10
            x = x // 10
            y = y * 10 + d

        if y.bit_length() < 32:
            if negative == True:
                return y * -1
            return y
        return 0
