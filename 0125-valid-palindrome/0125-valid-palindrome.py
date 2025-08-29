class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=''
        s=s.lower()
        for i in s:
            if i in  'abcdefghijklmnopqrstuvwxyz0123456789':
                st+=i
        return st==st[::-1]
        
             