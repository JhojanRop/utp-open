#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node {
    int id;
    long long w, p;
    
    bool operator<(const Node& other) const {
        return w * other.p < other.w * p;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> p(n + 1);
    vector<long long> w(n + 1);
    vector<int> parent(n + 1, 0);
    vector<int> dsu(n + 1);

    for (int i = 1; i <= n; ++i) cin >> p[i];
    for (int i = 1; i <= n; ++i) cin >> w[i];

    int m;
    cin >> m;
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        parent[u] = v;
    }

    long long ans = 0;
    for (int i = 1; i <= n; ++i) {
        ans += p[i] * w[i];
        dsu[i] = i;
    }
    
    dsu[0] = 0;
    w[0] = 0;
    p[0] = 0;

    auto find_root = [&](int i) {
        int root = i;
        while (root != dsu[root]) {
            root = dsu[root];
        }
        int curr = i;
        while (curr != root) {
            int nxt = dsu[curr];
            dsu[curr] = root;
            curr = nxt;
        }
        return root;
    };

    priority_queue<Node> pq;
    for (int i = 1; i <= n; ++i) {
        pq.push({i, w[i], p[i]});
    }

    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();

        int v = current.id;
        
        if (dsu[v] != v) continue;
        if (w[v] != current.w || p[v] != current.p) continue;

        int u = find_root(parent[v]);

        ans += p[u] * w[v];
        p[u] += p[v];
        w[u] += w[v];
        dsu[v] = u;

        if (u != 0) {
            pq.push({u, w[u], p[u]});
        }
    }

    cout << ans << "\n";

    return 0;
}
