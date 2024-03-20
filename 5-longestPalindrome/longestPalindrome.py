class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        This is work for the LPS.
        :param s: the string input.
        :return: the result of string.
        """
        # dp[i][j] indicate the number of sting i and j,
        # the ij should start the end of string and then i move left,
        # and j move right.

        length = len(s)

        # 设置数组 dp，用来存储字符串 s 的 [i,j] 区间的子串是否是回文子串
        # dp[0][0] 表示字符串 s 第 0 个字符和字符串 s 第 0 个字符之间的子串是否是回文子串
        # dp[2][3] 表示字符串 s 第 2 个字符和字符串 s 第 3 个字符之间的子串是否是回文子串
        # dp[i][j] 表示字符串 s 第 i 个字符和字符串 s 第 j 个字符之间的子串是否是回文子串
        # i 最大值为 length - 1
        dp = [[False] * length for _ in range(length)]

        # dp[0][0] 表示字符串 s 第 0 个字符和字符串 s 第 0 个字符之间的的子串是否是回文子串
        # dp[3][3] 表示字符串 s 第 3 个字符和字符串 s 第 3 个字符之间的的子串是否是回文子串
        # dp[i][i] 表示字符串 s 第 i 个字符和字符串 s 第 i 个字符之间的的子串是否是回文子串
        # 此时，这个区间的字符只有一个，肯定是回文子串
        for i in range(length):
            dp[i][i] = True

        # 设置变量记录最长的回文子串的长度
        maxLen = 1

        # 设置变量记录最长的回文子串的开始位置
        # 从后向前寻找
        begin = length - 1

        # i 从字符串 s 的【尾部】开始向前遍历，j 从 i + 1 开始向后遍历
        # 不断的逼近二维数组最右上角的位置，即求 dp[0][length - 1]
        for i in range(length - 1, -1, -1):

            for j in range(i + 1, length):

                # 如果发现 s.charAt(i) == s.charAt(j)
                if s[i] == s[j]:

                    # 如果 [i , j] 这个区间中只有 2 个字符，并且此时两个字符还是一样的
                    # 那么肯定是回文子串
                    # 假设 i = 5， j = 6，[i , j] 这个区间中只有 2 个字符
                    # 如果不加这个判断的话，dp[i][j] = dp[ i + 1 ][ j - 1 ]
                    # 此时，i + 1 = 6， j - 1 = 5
                    # [ 6 , 5 ] 这个区间不存在，默认值为 false
                    if (j - i + 1) == 2:

                        dp[i][j] = True

                    else:

                        # 否则，当前这个区间是否是回文子串区间取决于 [ i + 1 , j - 1 ] 这个区间
                        dp[i][j] = dp[i + 1][j - 1]



                else:
                    # 如果发现 s.charAt(i) ！= s.charAt(j)
                    # 那说明 [i , j] 这个区间必然不是回文子串
                    dp[i][j] = False

                # 更新最长的回文子串长度
                if dp[i][j] and j - i + 1 > maxLen:
                    # 更新最长的回文子串长度
                    maxLen = j - i + 1
                    # 更新最长的回文子串的开始位置
                    begin = i

        # 通过截取的方式返回最长的回文子串
        return s[begin:begin + maxLen]



