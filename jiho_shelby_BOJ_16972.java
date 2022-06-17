/**
 * https://boj.kr/16972
 * 구성적 알고리즘 문제풀이
 * 전체 좌표평면을 29*29 크기로 슬라이싱 후 랜덤으로 좌표를 찍는 방식으로 
 */

class Main {

    static final int OFFSET = 561;
    static final long MAX_VALUE = 1L << 62;

    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {

        Point[][] points = new Point[29][29];

        for (int r = 0; r < 29; r++) {
            for (int c = 0; c < 29; c++) {
                points[r][c] = getRandomPoint(r, c);
            }
        }

        long minDist = 1L << 61;

        for (int i = 0; i < 814; i++) {
            int r = i / 29;
            int c = i % 29;

            long topDist = MAX_VALUE;
            long leftDist = MAX_VALUE;

            if (r > 0) topDist = calculateDist(points[r - 1][c], points[r][c]);
            if (c > 0) leftDist = calculateDist(points[r][c - 1], points[r][c]);

            long dist = Math.min(topDist, leftDist);

            if (minDist > dist) {
                minDist = dist;
            } else if (minDist == dist) {
                points[r][c] = getRandomPoint(r, c);
                i--;
            }
        }

        for (int i = 0; i < 814; i++) {
            int r = i / 29;
            int c = i % 29;
            write(points[r][c].x);
            write(points[r][c].y);
            newLine();
        }

        flush();

    }

    static long calculateDist(Point a, Point b) {
        long dx = Math.abs(a.x - b.x);
        long dy = Math.abs(a.y - b.y);
        return dx + dy;
    }

    static Point getRandomPoint(int r, int c) {
        int x = (int) ((Math.random() + r) * OFFSET) - 8140;
        int y = (int) ((Math.random() + c) * OFFSET) - 8140;
        return new Point(x, y);
    }

    static int idx, SIZE = 1 << 13;
    static byte[] buf = new byte[SIZE];

    static void write(int n) {
        int num = n < 0 ? ~n + 1 : n;
        int l = num <= 1 ? 1 : (int) (Math.log10(num) + 1);
        if (n < 0) {
            l++;
            if (idx + l >= SIZE) flush();
            int i = idx + l;
            while (num > 0) {
                buf[--i] = (byte) (num % 10 | 48);
                num /= 10;
            }
            buf[--i] = 45;
            idx += l;
            buf[idx++] = 32;
        } else {
            if (idx + l >= SIZE) flush();
            int i = idx + l;
            while (num > 0) {
                buf[--i] = (byte) (num % 10 | 48);
                num /= 10;
            }
            idx += l;
            buf[idx++] = 32;
        }
    }

    static void newLine() {
        buf[idx - 1] = 10;
    }

    static void flush() {
        System.out.write(buf, 0, idx);
        idx = 0;
    }

}
