# Hard
# This problem was asked by Amazon.

# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".


from functools import cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        @cache
        def helper(start, end):
            if end - start <= 0:
                return True
            elif s[start] != s[end]:
                return False
            else:
                return helper(start + 1, end - 1)

        start = 0
        end = 0

        for st in range(len(s)):
            for en in range(st, len(s)):
                if helper(st, en) and en - st > end - start:
                    start = st
                    end = en

        return s[start : end + 1]


# Top down approach

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         @cache
#         def helper(start, end):
#             if end - start <= 0:
#                 return True
#             elif s[start] != s[end]:
#                 return False
#             else:
#                 return helper(start + 1, end - 1)

#         start = 0
#         end = len(s) - 1

#         while end >= 0:

#             for x in range(len(s) - 1 - end + 1):
#                 if helper(start + x, end + x):
#                     return s[start + x : end + x + 1]
#             end -= 1
