class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        l=[]
        for val in freq.values():
            l.append(val)
        if len(l)==len(set(l)):
            return True
        else:
            return False
                