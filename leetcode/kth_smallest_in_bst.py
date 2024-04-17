"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""


class TreeNode:
    def __init__(self, root, left=None, right=None) -> None:
        self.val = root
        self.left = left
        self.right = right


def kth_smallest(root, k):

    def inorder(node: TreeNode):
        if node is None:
            return

        nonlocal count, res
        inorder(node.left)

        count += 1

        if node.val == k:
            res = node.val
            return
        inorder(node.right)

    count = 0
    res = None

    inorder(root)
    return res


# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

k = 5

print(kth_smallest(root, k))
