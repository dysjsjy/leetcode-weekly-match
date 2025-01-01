package com.dysjsjy;

public class F1457 {

    int count = 0;

    public int pseudoPalindromicPaths(TreeNode root) {
        int[] ins = new int[10];
        travelTree(root, ins);
        return count;
    }

    void travelTree(TreeNode root, int[] ints) {
        if (root == null) return;

        ints[root.val]++;

        if (root.left == null && root.right == null) {
            int cnt = 0;
            for (int i : ints) {
                if (i % 2 != 0) {
                    cnt++;
                }
            }
            if (cnt <= 1) {
                count++;
            }
        }

        travelTree(root.left, ints);
        travelTree(root.right, ints);

        //回溯是都要回溯的
        ints[root.val]--;
    }

    private int pseudoPalindromicPaths2(TreeNode root) {
        int[] p = new int[10];
        return dfs2(root, p);
    }

    private int dfs2(TreeNode node, int[] p) {
        if (node == null) return 0;

        p[node.val] ^= 1;
        int res;
        if (node.left == node.right) {
            res = count2(p) <= 1 ? 1 : 0;
        } else {
            res = dfs2(node.left, p) + dfs2(node.right, p);
        }
        p[node.val] ^= 1;
        return res;
    }

    private int count2(int[] p) {
        int cnt = 0;
        for (int x : p) {
            cnt += x;
        }
        return cnt;
    }

    private int pseudoPalindromicPaths3(TreeNode root) {
        return dfs3(root, 0);
    }

    private int dfs3(TreeNode root, int mask) {
        if (root == null) return 0;
        mask ^= 1 << root.val;
        if (root.left == root.right) {
            return (mask & (mask - 1)) == 0 ? 1 : 0;
        }
        return dfs3(root.left, mask) + dfs3(root.right, mask);
    }
}





//错误写法
//List<List<Integer>> res = new ArrayList<>();
//
//public int pseudoPalindromicPaths (TreeNode root) {
//    List<Integer> path = new ArrayList<>();
//    int[] ints = new int[10];
//    travelTree(root, path, ints);
//
//    return res.size();
//}
//
//void travelTree(TreeNode root, List<Integer> path, int[] ints) {
//    if (root == null) return;
//
//    path.add(root.val);
//    ints[root.val]++;
//
//    if (root.left != null) {
//        travelTree(root.left, path, ints);
//        path.remove(path.size() - 1);
//        ints[path.get(path.size() - 1)]--;
//    }
//
//    if (root.right != null) {
//        travelTree(root.right, path, ints);
//        path.remove(path.size() - 1);
//        ints[path.get(path.size() - 1)]--;
//    }
//
//    if (root.left == null && root.right == null) {
//        int cnt = 0;
//
//        for (int i : ints) {
//            if (i %2 != 0) cnt++;
//        }
//
//        if (cnt <= 1) {
//            res.add(new ArrayList<>(path));
//        }
//    }
//}