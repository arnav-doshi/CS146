from typing import List

class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        setted = set()

        length = len(nums)
        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(j+1,length):
                    if (nums[i]+nums[j]+nums[k]) == 0:
                        setted.add((nums[i],nums[j],nums[k]))
        
        if len(setted) == 0:
            return []
        else:
            return setted


three_sum = ThreeSum()
nums = [-5, 0, 5, 10, -10, 0] 
print(three_sum.threeSum(nums))
