#include <iostream>
#include <vector>
#include <limits>

using namespace std;

void solve() {
    int n;
    cin >> n;
    
    // Use vector for dynamic sizing
    vector<int> arr(n);
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // Initialize mx to the smallest possible integer
    int mx = numeric_limits<int>::min();
    for(int i = 0; i < n; i++) {
        mx = max(mx, arr[i]);
    }
    
    cout << mx << endl;
}

int main() {
    solve();
    return 0;
}
