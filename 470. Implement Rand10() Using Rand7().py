# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        c = rand7()
        while c > 5:
            c = rand7()

        if self.biny():
            return 5 + c
        return c

    # make a random binary choice
    def biny(self):
        c = rand7()
        if c == 4:
            return self.biny()
        else:
            return c > 4
