class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        # sorted dic=dict(sorted(a.items(), key=lambda x: x[1],reverse=True ))
        b=[]
        for i in range(k):
            key=max(a, key=a.get)
            b.append(key)
            a.pop(key)
            
        return b