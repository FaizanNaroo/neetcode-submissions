class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=[]
        for i in range(len(s)):
            chara=s[i]
            if chara.isalnum():
                str.append(s[i].lower())

        for i in range(len(str)//2):
            if str[i] != str[len(str)-i-1]:
                return False
        return True

        

        