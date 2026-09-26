#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    int num_components;
    int max_size;

    DSU(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        sz.assign(n + 1, 1);
        num_components = n;
        max_size = 1;
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            if (sz[root_i] < sz[root_j])
                swap(root_i, root_j);
            parent[root_j] = root_i;
            sz[root_i] += sz[root_j];
            num_components--;
            if (sz[root_i] > max_size) {
                max_size = sz[root_i];
            }
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, P;
    while (cin >> N >> P && (N != 0 || P != 0)) {
        DSU dsu(N);
        for (int i = 0; i < P; ++i) {
            int u, v;
            cin >> u >> v;
            dsu.unite(u, v);
        }
        cout << dsu.num_components << " " << dsu.max_size << "\n";
    }

    return 0;
}
