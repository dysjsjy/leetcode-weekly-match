

def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None
    
    # 递归构建左右子树的新树
    left = self.removeLeafNodes(root.left, target)
    right = self.removeLeafNodes(root.right, target)
    
    # 如果左右子树都为 None 且当前节点值等于目标值，则返回 None 表示删除该节点
    if left is None and right is None and root.val == target:
        return None
    
    # 创建新节点，构建新的子树
    return TreeNode(root.val, left, right)
