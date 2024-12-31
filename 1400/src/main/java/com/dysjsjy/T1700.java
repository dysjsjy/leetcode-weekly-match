package com.dysjsjy;

import java.util.*;

public class T1700 {


    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < students.length; i++) {
            queue.offer(students[i]);
        }

        int p = 0;
        while (true) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int a = queue.poll();
                if (a == sandwiches[p]) {
                    p++;
                } else {
                    queue.offer(a);
                }
            }

            if (queue.size() == size) {
                return size;
            }
        }
    }

    public int countStudents1(int[] students, int[] sandwiches) {
        int s1 = Arrays.stream(students).sum();
        int s0 = students.length - s1;

        for (int i = 0; i < sandwiches.length; i++) {
            if (sandwiches[i] == 0 && s0 > 0) {
                s0--;
            } else if (sandwiches[i] == 1 && s1 > 0) {
                s1--;
            } else {
                break;
            }
        }

        return s0 + s1;
    }
}
