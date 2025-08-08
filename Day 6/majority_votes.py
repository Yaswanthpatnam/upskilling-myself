class Solution:
    def findMajority(self, arr):
        # code here
        n = len(arr)
        dict = {}
        res = []
        
        for ele in arr:
            dict[ele] = dict.get(ele,0)+1
        for ele, cnt in dict.items():
            if cnt > n//3:
                res.append(ele)
        if len(res) == 2 and res[0] > res[1]:
            res[0],res[1] = res[1],res[0]
        return res    