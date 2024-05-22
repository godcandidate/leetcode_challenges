class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_s = []

        for l in s:
            if l.isalnum():
                list_s.append(l.lower())
        
        return list_s == list(reversed(list_s))
        
