class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        container = set()
        start = 0
        end = 0
        maxlength = 0

        while end < len(s):
            if s[end] in container:
                container.remove(s[start])
                start += 1
            else:
                container.add(s[end])
                length = end - start + 1
                maxlength = max(maxlength, length)
                end += 1

        return maxlength
