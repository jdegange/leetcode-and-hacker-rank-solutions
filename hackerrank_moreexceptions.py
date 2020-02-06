#Write your code here
class Calculator():
        def power(self,n,p):
            if n >= 0 and p >= 0:
                power = n**p
            else:
                power = 'n and p should be non-negative'
            return power

myCalculator=Calculator()
