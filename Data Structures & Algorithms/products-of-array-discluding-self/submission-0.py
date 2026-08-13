class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=[]
        c.append(nums[0])
        for i in range (1,len(nums)):
            c.append(c[i-1]*nums[i])
       

        l=[]
        l.append(nums[-1])
        r=len(nums)
        for i in range(len(nums)-2,-1,-1):
            l.append(nums[i] *l[r-i-2])
            
        l.reverse()
        

        s=[]
        for i  in range(r):
            if i==0:
                s.append(l[i+1])
            elif i==r-1:
                s.append(c[r-2])
            else:
                s.append(c[i-1]*l[i+1])
        return s

