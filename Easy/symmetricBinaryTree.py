def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def mirror(left, right):
            if left and right:
                if left.val == right.val:
                    truthy_a = mirror(left.left, right.right)
                    truthy_b = mirror(left.right, right.left)
                    return truthy_a and truthy_b
                else:
                    return False
            elif not left and not right:
                return True
            else:
                return False

        return mirror(root.left, root.right)
