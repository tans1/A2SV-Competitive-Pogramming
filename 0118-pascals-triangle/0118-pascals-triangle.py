class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            temp = [1]
            for j in range(1,i):
                cur = ans[-1][j-1] + ans[-1][j]
                temp.append(cur)
            if i != 0:
                temp.append(1)
            ans.append(temp)
        
        return ans
            