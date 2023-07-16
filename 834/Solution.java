import java.util.ArrayList;
import java.util.List;

class Solution {
    int[] dp;
    int[] sz;
    int[] res;
    List<List<Integer>> graph;

    public void dfs_1(int child, int father) {
        sz[child] = 1;
        dp[child] = 0;
        for (int item: graph.get(child)) {
            if (item == father) {
                continue;
            }
            dfs_1(item, child);
            dp[child] += dp[item] + sz[item];
            sz[child] += sz[item];
        }
    }

    public void dfs_2(int child, int father) {
        res[child] = dp[child];
        for (int item: graph.get(child)) {
            if (item == father) {
                continue;
            }
            int pu = dp[child], pv = dp[item];
            int su = sz[child], sv = sz[item];

            dp[child] -= dp[item] + sz[item];
            sz[child] -= sz[item];
            dp[item] += dp[child] + sz[child];
            sz[item] += sz[child];

            dfs_2(item, child);

            dp[child] = pu;
            dp[item] = pv;
            sz[child] = su;
            sz[item] = sv;
        }
    }

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        dp = new int[n];
        sz = new int[n];
        res = new int[n];
        graph = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for (int[] edge: edges) {
            int x = edge[0], y = edge[1];
            graph.get(x).add(y);
            graph.get(y).add(x);
        }
        
        dfs_1(0, -1);
        dfs_2(0, -1);

        return res;
    }
}