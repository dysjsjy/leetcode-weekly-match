package com.dysjsjy;

import java.util.*;
import java.util.stream.IntStream;

public class F1508 {


    public int rangeSum(int[] nums, int n, int left, int right) {
        int[] pd = new int[n * (n + 1) / 2];
        int pdi = 0, ans = 0, mod = 1000000007;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                pd[pdi++] = sum;
            }
        }
        Arrays.sort(pd);
        for (int i = left - 1; i < right; i++) {
            ans += pd[i];
            ans %= mod;
        }
        return ans;
    }

    //my
    public int rangeSum2(int[] nums, int n, int left, int right) {
        final int MODULO = 1000000007;
        List<Integer> list = new ArrayList<>();


        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                list.add(sum);
            }
        }

        Collections.sort(list);

        int ans = 0;

        for (int i = left - 1; i < right; i++) {
            ans = (ans + list.get(i)) % MODULO;
        }

        return ans;
    }
}
