class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """
    def SquareArray(self, A):
        #
        res = list(map(lambda x:x**2, A))
        res.sort()
        return res
 #思路
 #额  我猜测  肯定不应该这么憨憨
 #是不是有更好的方法呢
 #没get到