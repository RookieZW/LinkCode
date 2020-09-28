'''
描述
手机号码由且仅由 N 位十进制数字(0-9)组成。一个手机号码中有至少 k 位数字相同则被定义为靓号。
手机号可以有前导零，比如 000123456 是一个合法的手机号。
小多想花钱将自己的手机号码修改为一个靓号。修改号码中的一个数字需要花费的金额为新数字与旧数字之间的差值的绝对值。
比如将 1 修改为 6 或 6 修改为 1 都需要花 5 块钱。
给定一个长度为N的整型数组number作为小多现在的手机号码，问将其修改成一个靓号，花费最少的靓号是哪一个？
如果有多个靓号花费最少，那么返回字典序最小的靓号。
'''
class Solution:
    """
    @param number: the old phone number array
    @param k: at least k same number
    @return: return the minium beautiful number
    """
    def getMiniumNumber(self,number, k):
        # write your code here
        n = number
        number_len = len(number)
        print(number_len)
        if number_len == k:
            return "".join([str(min(number))] * number_len)
        set_number = sorted(list(set(n)))
        count = [0] * 10
        for i in n:
            count[i] += 1  # 计数
        cost = [0] * 10
        print(count)
        for i in range(10):
            j = count[i]  # 记录数量
            pre = i - 1  # 往前
            after = i + 1  # 往后
            while True:
                if j == k:
                    break
                else:
                    if pre < 0:
                        if k - j <= count[after]:
                            cost[i] += (k - j) * (after - i)
                            break
                        else:
                            j += count[after]
                            cost[i] += (after - i) * count[after]
                            after += 1
    
                    elif after > 9:
                        if k - j <= count[pre]:
                            cost[i] += (k - j) * (i - pre)
                            break
                        else:
                            j += count[pre]
                            cost[i] += (i - pre) * count[pre]
                            pre -= 1
                    else:
                        if k - j <= count[after]:
                            cost[i] += (k - j) * (after - i)
                            break
                        else:
                            j += count[after]
                            cost[i] += (after - i) * count[after]
                            after += 1
                            
                        if k - j <= count[pre]:
                            cost[i] += (k - j) * (i - pre)
                            break
                        else:
                            j += count[pre]
                            cost[i] += (i - pre) * count[pre]
                            pre -= 1
                        
        print(cost)
        cost.reverse()
        while True:
            min_cost = min(cost)
            index = cost.index(min_cost)
            if (9-index) in set_number:
                break
            cost[index] = 9999
        index = 9 -index
        pre = index - 1
        after = index + 1
        replace_pre = []
        replace_after = []
        j = count[index]
        print("start")
        while True:
            if j == k:
                return "".join([str(x) for x in number])

            if after <= 9:
                if j + count[after] >= k:
                    replace_after.append(k - j)
                    break
                else:
                    j += count[after]
                    replace_after.append(count[after])
                    after += 1
                    
            if pre >= 0:
                if j + count[pre] >= k:
                    replace_pre.append((k - j))
                    break
                else:
                    j += count[pre]
                    replace_pre.append(count[pre])
                    pre -= 1
        
        pre_len = len(replace_pre)
        after_len = len(replace_after)
        for i in range(number_len):
            if number[i] > index and 0<number[i] - index <= after_len:
                if number[i] == 9:
                    print(replace_after[9-index-1])
                if replace_after[number[i] - index-1] > 0:
                    replace_after[number[i] - index-1] -= 1
                    number[i] = index
                    
            elif number[i] < index and 0< index - number[i] <= pre_len:
    
                if replace_pre[index - number[i]-1] < count[number[i]]:
                    count[number[i]] -= 1
                else:
                    replace_pre[index - number[i]-1] -= 1
                    count[number[i]] -= 1
                    number[i] = index
                    
        return "".join([str(x) for x in number])
# 思路
#暴力搜索   （这答案居然超过了百分百玩家  说实话有点惊讶）
#第一步  经计算每一个数字变成靓号的代价
#第二步  确定是哪个数的代价最低
#第三步  计算转成靓号需要改的数字及个数   有题目要求   先转大的数字
#第四步  最骚的地方   注意不是全部转换的数字   需要判断是对前n个转换还是后n个转换