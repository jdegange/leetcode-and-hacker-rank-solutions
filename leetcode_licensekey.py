class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()
        if K == 1: 
            return "-".join(list(S))

        lst = []
        while len(S) >= K: 
            S, extra = S[0:-K], S[-K:len(S)]
            lst = [extra] + lst

        if len(S) > 0: 
            lst = [S] + lst
        return "-".join(lst)
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
