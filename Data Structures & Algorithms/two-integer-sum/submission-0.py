class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            t=target-nums[i]

            for j in range(i+1,len(nums)):
                if nums[j] == t:
                    a.append(i)
                    a.append(j)
                    return a
        

                    
        