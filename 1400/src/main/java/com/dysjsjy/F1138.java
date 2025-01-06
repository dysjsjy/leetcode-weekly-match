package com.dysjsjy;

import java.util.HashMap;

public class F1138 {

    public String alphabetBoardPath(String target) {
        StringBuilder sb = new StringBuilder();
        int x = 0, y = 0;
        for (char c : target.toCharArray()) {
            int nx = (c - 'a') / 5;
            int ny = (c - 'a') % 5;
            String v = nx < x ? "U".repeat(x - nx) : "D".repeat(nx - x);
            String h = ny < y ? "L".repeat(y - ny) : "R".repeat(ny - y);
            sb.append(c != 'z' ? v + h : h + v).append('!');
            x = nx;
            y = ny;
        }

        return sb.toString();
    }
}
