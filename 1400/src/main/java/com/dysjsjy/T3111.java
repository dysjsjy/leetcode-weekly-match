package com.dysjsjy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class T3111 {

    //这居然是一个滑动窗口
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        Arrays.sort(points, (o1, o2) -> {
            return Integer.compare(o1[0], o2[0]);
        });

        int right = Integer.MIN_VALUE;
        int count = 0;

        for (int i = 0; i < points.length; i++) {
            if (right < points[i][0]) {
                right = points[i][0] + w;
                count++;
            }
        }

        return count;
    }

    //我的错误写法
    public int minRectanglesToCoverPoints2(int[][] points, int w) {
        Arrays.sort(points, (a, b) -> {
            return Integer.compare(a[0], b[0]);
        });

        List<int[]> list = new ArrayList<>();

        for (int i = 0; i < points.length; i++) {
            int x1 = points[i][0];

            for (int j = points.length - 1; j >= 0 ; j--) {
                int x2 = points[j][0];

                if (x1 > x2) {
                    break;
                }

                if (x2 - x1 <= w) {
                    int max = Integer.MIN_VALUE;
                    for (int k = i; k <= j; k++) {
                        if (max < points[k][0]) {
                            max = points[k][0];
                        }
                    }

                    list.add(new int[]{x2, max});
                    i = list.get(list.size() - 1)[0] + 1;
                    break;
                }
            }
        }

        return list.size();
    }
}
