class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ar1,ar2=[0]*26,[0]*26
        s=s.lower()
        t=t.lower()
        for i in s:
            ar1[ord(i)-97]+=1
        for i in t:
            ar2[ord(i)-97]+=1
        return ar1==ar2