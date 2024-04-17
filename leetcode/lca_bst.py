from basics.Tree import Tree


# LCA in BST
class LCAinBST:

    def lca_bst(self, root: Tree, p: Tree, q: Tree):
        if root is None:
            return root

        if root.val > p.val and root.val > q.val:
            return self.lca_bst(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lca_bst(root.right, p, q)

        return root

    # LCA in Binary tree

    def lca_binary_tree(self, root: Tree, p: Tree, q: Tree):

        if root is None:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lca_binary_tree(root.left, p, q)
        right = self.lca_binary_tree(root.right, p, q)

        if left and right:
            return root

        return left if left is not None else right
