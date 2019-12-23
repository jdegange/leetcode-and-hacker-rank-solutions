class Solution(object):
    def numUniqueEmails(self, emails):
        dict = {}
        for count, i in enumerate(emails):
            orig = i
            split = i.rsplit('@',1)
            prefix = split[0]
            suffix = split[1]
            prefix = prefix.split('+',1)[0] #trim to right of all '+'
            prefix = prefix.replace('.','') #remove dots '.'
            
            norm_add = prefix+"@"+suffix

            if norm_add not in dict.keys():
                dict[norm_add] = 1
            else:
                dict[norm_add] += dict[norm_add] +1
        return len(dict)  
            
        """
        :type emails: List[str]
        :rtype: int
        """
        
