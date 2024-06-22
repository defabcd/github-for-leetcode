class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # 문자열을 리스트로 변환하여 수정 가능하도록 함
        s = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # 좌우 문자가 다를 때, 사전식으로 더 작은 문자로 치환
                if s[left] < s[right]:
                    s[right] = s[left]
                else:
                    s[left] = s[right]
            left += 1
            right -= 1
        
        # 리스트를 다시 문자열로 변환하여 반환
        return ''.join(s)
#https://leetcode.com/problems/lexicographically-smallest-palindrome/