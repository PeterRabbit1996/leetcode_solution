'''
557. 反转字符串中的单词 III

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''


class Solution:
    # def reverseWords(self, s: str) -> str:
    def reverseWords(self, s):
        if s == None:
            return None

        # result = []
        # for word in s.split(' '):
        #     result.append(word[: : -1])

        # return ' '.join(result)

        return ' '.join(s[: : -1].split(' ')[: : -1])

if __name__ == '__main__':
    str = "Let's take LeetCode contest"
    s = Solution()
    print(s.reverseWords(str))











