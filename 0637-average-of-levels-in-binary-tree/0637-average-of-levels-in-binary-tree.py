# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        temp = defaultdict(list)
        
        def dfs(node, level):
            if node:
                temp[level].append(node.val)
                dfs(node.left, level + 1)
                dfs(node.right,level + 1)
        
        dfs(root, 1)
        ans = []
        srt = sorted(temp.items(), key = lambda x: x[0])
        for k, v in srt:
            ans.append(sum(v) / len(v))
        
        return ans
            