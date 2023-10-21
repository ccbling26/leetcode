import java.util.Arrays;

class Solution {
    public long countPairs(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        for (int[] edge : edges) {
            int x = edge[0], y = edge[1];
            uf.union(x, y);
        }
        long res = 0;
        for (int i = 0; i < n; i++) {
            res += n - uf.getSize(uf.find(i));
        }
        return res / 2;
    }
}

class UnionFind {
    int[] parents;
    int[] sizes;

    public UnionFind(int n) {
        parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        sizes = new int[n];
        Arrays.fill(sizes, 1);
    }

    public int find(int x) {
        if (parents[x] == x) {
            return x;
        } else {
            parents[x] = find(parents[x]);
            return parents[x];
        }
    }

    public void union(int x, int y) {
        int parentX = find(x), parentY = find(y);
        if (parentX != parentY) {
            if (sizes[parentX] > sizes[parentY]) {
                parents[parentY] = parentX;
                sizes[parentX] += sizes[parentY];
            } else {
                parents[parentX] = parentY;
                sizes[parentY] += sizes[parentX];
            }
        }
    }

    public int getSize(int x) {
        return sizes[x];
    }
}