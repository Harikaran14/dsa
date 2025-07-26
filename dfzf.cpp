#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t; 
    while (t--) {
        int n;
        cin >> n; 
        vector<int> x(n);

        for (int i = 0; i < n; ++i) {
            cin >> x[i]; 
        }

        vector<int> prefix_sums(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            prefix_sums[i] = prefix_sums[i - 1] + x[i - 1];
        }

        
        set<int> result;
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int subarray_sum = prefix_sums[j + 1] - prefix_sums[i];
                result.insert(subarray_sum);
            }
        }

        
        result.insert(0);

        
        vector<int> final(result.begin(), result.end());

        
        cout << final.size() << endl;
        for (size_t i = 0; i < final.size(); ++i) {
            cout << final[i];
            if (i != final.size() - 1) cout << " ";
        }
        cout << endl;
    }

    return 0;
}