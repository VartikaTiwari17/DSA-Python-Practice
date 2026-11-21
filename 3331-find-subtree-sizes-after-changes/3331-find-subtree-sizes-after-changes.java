class Solution {
    List<List<Integer>>adj;
    int sub[];
    int yo[];
    int diff[];
    int ans[];
    String s;
    public void helper(int node, int par){
        sub[node]++;
        char c = s.charAt(node);
        int prevVal = yo[c-'a'];
        yo[c-'a'] = node;
        for(int neigh: adj.get(node)){
            if(neigh == par) continue;

            helper(neigh, node);
            sub[node] += sub[neigh];
        }
        yo[c-'a'] = prevVal;
        sub[node] += diff[node];
        ans[node] = sub[node];
        if(prevVal != -1 && par != -1){
            diff[par] += -1*(sub[node]);
            diff[prevVal] += sub[node];
        }
    }
    public int[] findSubtreeSizes(int[] parent, String s) {
        adj = new ArrayList<>();
        int n = parent.length;
        this.s = s;
        yo = new int[26];
        diff = new int[n];
        ans = new int[n];
        Arrays.fill(yo, -1);
        sub = new int[n];
        for(int i = 0; i < n;i++){
            adj.add(new ArrayList<>());
        }
        for(int i = 1; i < n;i++){
            adj.get(i).add(parent[i]);
            adj.get(parent[i]).add(i);
        }

        helper(0, -1);
        return ans;
    }
}