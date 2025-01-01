package com.dysjsjy;

public class T3101 {

    public long countAlternatingSubarrays(int[] nums) {
        long ans = 0;
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] != nums[i - 1]) {
                ++count;
            } else {
                count = 1;
            }
            ans += count;
        }
        return ans;
    }
}
