class Solution:
    def productExceptSelf(self, nums):

        answer = [1]*len(nums)
        answer[0] = 1
        
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * rightProduct
            rightProduct *= nums[i]
        return answer
        
