# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ConstTree(nums, index):
    if index=0:
        return


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Tree = ConstTree(root,len(root))

if __name__ == '__main__':
    print(Solution.rob([3,2,3,"null",3,"null",1]))