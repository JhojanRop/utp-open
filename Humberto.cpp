#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (cin >> t) {
        while (t--) {
            double r, R, h;
            cin >> r >> R >> h;
            if (R == r) {
                cout << fixed << setprecision(9) << (h / 2.0) << "\n";
            } else {
                double r_x = cbrt((pow(R, 3) + pow(r, 3)) / 2.0);
                double h_x = h * (r_x - r) / (R - r);
                
                cout << fixed << setprecision(9) << h_x << "\n";
            }
        }
    }
    return 0;
}