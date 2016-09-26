class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        S = set(s)
        if len(s) == len(S):
            return len(s)

        max_len = 0

        for i in range(len(s)):
            temp_s = s[i]
            for j in range(i + 1, len(s)):
                if temp_s.find(s[j]) == -1:
                    temp_s += s[j]
#                     if j == len(s) - 1:
#                         temp.append(temp_s)
                else:
                    #                     temp.append(temp_s)
                    break

            if len(temp_s) > max_len:
                max_len = len(temp_s)
            if max_len == len(s) - i:
                return max_len

        print(temp)
        return max_len


if __name__ == '__main__':

    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sol = Solution()
    length = sol.lengthOfLongestSubstring(s)
    print(length)
    pass
