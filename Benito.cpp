#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int R, C;
    while (cin >> R >> C && (R != 0 || C != 0)) {
        string grid = "";
        grid.reserve(R * C);
        int start_pos = -1;

        for (int i = 0; i < R; ++i) {
            string row;
            cin >> row;
            if (start_pos == -1) {
                size_t pos = row.find('*');
                if (pos != string::npos) {
                    start_pos = i * C + pos;
                }
            }
            grid += row;
        }

        vector<int> stack;
        stack.reserve(R * C);
        stack.push_back(start_pos);
        
        grid[start_pos] = '#';
        int count = 0;

        while (!stack.empty()) {
            int pos = stack.back();
            stack.pop_back();
            count++;

            int r = pos / C;
            int c = pos % C;

            if (r > 0 && grid[pos - C] == '.') {
                grid[pos - C] = '#';
                stack.push_back(pos - C);
            }
            if (r < R - 1 && grid[pos + C] == '.') {
                grid[pos + C] = '#';
                stack.push_back(pos + C);
            }
            if (c > 0 && grid[pos - 1] == '.') {
                grid[pos - 1] = '#';
                stack.push_back(pos - 1);
            }
            if (c < C - 1 && grid[pos + 1] == '.') {
                grid[pos + 1] = '#';
                stack.push_back(pos + 1);
            }
        }
        
        cout << count << "\n";
    }
    
    return 0;
}
