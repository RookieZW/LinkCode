class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        t = s.split()
        t.reverse()
        s = " ".join(t)
        return s