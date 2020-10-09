'''
给定一个非空字符串 word 和缩写 abbr，返回字符串是否可以和给定的缩写匹配。
比如一个 “word” 的字符串仅包含以下有效缩写：

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
样例
样例 1:

输入 : s = "internationalization", abbr = "i12iz4n"
输出 : true
样例 2:

输入 : s = "apple", abbr = "a2e"
输出 : false
注意事项
注意只有以上缩写是字符串 word 合法的缩写。任何其他关于 word 的缩写都是不合法的。
'''
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def get_num(self, t, j):
        num = 0
        while j < len(t) and t[j].isdigit():
            num = num * 10 + int(t[j]) # * and then + 
            j += 1 
        return j, num
    
    def validWordAbbreviation(self, word, abbr):
        s = word
        t = abbr
        # s: original word t: abbreviation
        if not s or not t:
            return False 
        i, j = 0, 0
        #s, t = list(word), list(abbr)
        ls, lt = len(s), len(t)
        while i < ls and j < lt:
            if t[j] == '0':
                return False 
            if t[j].isdigit():
                j, num = self.get_num(t,j)
                i += num 
            else:
                if s[i] != t[j]: 
                    return False 
                i += 1 
                j += 1 
        return i == ls and j == lt