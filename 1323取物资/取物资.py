'''
在一个二维地图上有很多军营，每个军营的坐标为（x,y），有一条平行于y轴且长度无限的路，补给车经过这条路时会将每个军营的物资放到离他们军营最近的路边(这条马路所在的位置使得所有军营到达马路的距离和最小)，请问所有军营到马路的最短距离和是多少

样例
样例

输入:
[[-10,0],[0,0],[10,0]]
输出:20
说明:假设路在x=0上，最短路径和为10+0+10=20
'''
class Solution:
    """
    @param coordinates: a series of coordinates (x, y)
    @return: Given a series of coordinates (x, y),return the shortest sum of distance
    """
    def Fetchsupplies(self, coordinates):
        # write your code here
        coordinate = [x[0] for x in coordinates]
        coordinate.sort()
        middle = len(coordinate) // 2
        middle_value = coordinate[middle]
        count = 0
        for i in coordinate:
            count += abs(i -middle_value)
        return count
'''
中位数 作为中心
'''