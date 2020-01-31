class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            else:
                if abs(dict[nums[i]]-i) <= k:
                    print(dict[nums[i]],i)
                    return True
                else:
                    dict[nums[i]] = i
        return False

        
