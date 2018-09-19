class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        result = 0
        lists=[]
        for i in range(0,n+1):
            if str(k) in str(i):
                lists.append(i)
        for j in lists:
            count_tmp = str(j).count(str(k))
            result += count_tmp
        return result
print(Solution().digitCounts(7,123124))