class Solution(object):
    def reverse(self, x):
        if x < 0:
            orig = str(x).replace("-",'')
            value = int('-'+orig[::-1])
        elif x > 0:
            value = int(str(x)[::-1])
        if x == 0 or abs(value) > (2**31 -1):
            value = 0
        return value
