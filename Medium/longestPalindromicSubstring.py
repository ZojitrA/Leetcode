class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        pointa = 0
        pointb = 0

        for i in range(1, len(s)):
            for l in range(2):
                j = i + l
                k = i - 1
                while k >= 0 and j < len(s):

                    if s[k] != s[j]:
                        break

                    if j - k > pointb - pointa:
                        pointb = j
                        pointa = k
                    k-=1
                    j+=1

        return s[pointa:pointb+1]
