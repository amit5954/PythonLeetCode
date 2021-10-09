class Solution:
    def isPalindrome(self, x):
        rev = 0
        temp = x
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if temp == rev:
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome(-11))
print(a.isPalindrome(10))
print(a.isPalindrome(0))
print(a.isPalindrome(425))
print(a.isPalindrome(11))
print(a.isPalindrome(1221))

