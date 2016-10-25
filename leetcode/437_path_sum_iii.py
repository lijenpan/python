"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
==============================

"""


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        sum_dict = {0: 1}

        def dfs(p, target, path_sum, sum_dict):
            if p:
                path_sum += p.val
                diff = path_sum - target
                if diff in sum_dict:
                    self.count += sum_dict[diff]
                sum_dict[path_sum] = sum_dict.get(path_sum, 0) + 1
                dfs(p.left, target, path_sum, sum_dict)
                dfs(p.right, target, path_sum, sum_dict)
                sum_dict[path_sum] -= 1

        dfs(root, sum, 0, sum_dict)
        return self.count
