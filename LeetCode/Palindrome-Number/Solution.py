1class Solution:
2    def isPalindrome(self, x):
3        if x < 0:
4            return False
5
6        s = str(x)
7
8        return s == s[::-1]