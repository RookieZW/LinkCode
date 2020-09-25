'''
给定一个密文，和一个解密规则如下：对密文中的每个字母做变换，不同的字母不能变化到同一个字母。
例如banana ->xyzyzy这是一个有效的转换，但banana不可以变成xyyyyy，因为这样就没法解密回来。
现在输入一个很长的字符串，判断该字符串是否存在子串可符合以上的加密解密规则。如果存在，返回字符串"yes"，否则返回字符串"no".

样例
样例 1:

给定 `s="abcabcd"`, `word="xyzxyz"`, 返回 `"yes"`.
输入：
abcabcd
xyzxyz
输出：
yes

解释:
"x" 可以变换为 "a", "y" 可以变换为 "b" ，"z" 可以变换为 "c".
样例 2：

给定 `s="abca"`, `word="xyzd"`, 返回 `"no"`.
输入：
abca
xyzd
输出：
no

解释:
单词 "xyzd" 没有办法变成 "abca".
注意事项
密文的长度不超过1010
字符串的长度不超过1000010000
字符串全部由小写字母完成
'''


class Solution:
    """
    @param s: the long string
    @param word: the secrect word
    @return: whether a substring exists in the string can be transformed by the above encoding rule
    """
    def getAns(self, s, word):
        # Write a code here
        assert(len(word) <= 10)
        assert(len(s) <= 10000)
        dic = {}
        w_len = len(word)
        s_len = len(s)
        i = 0
        j = 0
        value_set = set([])
        while i < s_len:
            if s[i] in dic:
                if dic[s[i]] == word[j]:
                    i+=1
                    j+=1
                else:
                    del dic
                    dic = {}
                    value_set.clear()
                    i+=1
                    j = 0
            else:
                dic[s[i]] = word[j]
                v_len = len(value_set)
                value_set.add(word[j])
                if v_len == len(value_set):
                    del dic
                    dic = {}
                    value_set.clear()
                    i+=1
                    j = 0
                else:
                    i+=1
                    j+=1
            if j >= w_len:
                
                return 'yes'
        return 'no'
#思路
#1、暴力查找子串的思想
#2、利用字典记录每个相同key对应的value是否相同
#3、利用集合记录每个key的value不能相同