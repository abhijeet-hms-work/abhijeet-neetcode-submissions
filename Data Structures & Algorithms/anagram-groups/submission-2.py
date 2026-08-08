class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def Anagrams(str1,str2):
        #     a={}
        #     b={}
        #     if len(str1) != len(str2):
        #         return False
        #     for i in str1:
        #         if i in a.keys():
        #             a[i] += 1
        #         else:
        #             a[i]=1
        #     for j in  str2:
        #         if j in b.keys():
        #             b[j] += 1
        #         else:
        #             b[j]=1
        #     if a==b:
        #         return True
        #     else:
        #         return False
        
        # c=[]
        # s=[]
        # for i in range(len(strs)):
        #     d=[]
        #     if strs[i] not in s:
        #         for j in range(i+1,len(strs)):
        #             bol=Anagrams(strs[i],strs[j])
        #             if bol == True :
        #                 d.append(strs[j])
        #                 s.append(strs[j])
        #         d.append(strs[i])
        #         s.append(strs[i])
        #         # print(d)
        #     if d:
        #         c.append(d)
        # return c
        a={}
        for i in strs:
            b=[0]*26

            for ch in i:
                b[ord(ch)-ord("a")]+=1
            if tuple(b) not in a:
                a[tuple(b)]=[]
            a[tuple(b)].append(i)
        c=[]
        for value in a.values():
            c.append(value)
        return c

        