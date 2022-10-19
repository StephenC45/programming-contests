/*
Solution to Problem A (Marathon) from Codeforces Round 799 Division 4.
*/



#include <bits/stdc++.h>

#define int long long

using namespace std;



int32_t main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    // Read the number of test cases.
    int test_count;
    cin >> test_count;

    // Process each test case.
    for (int tc = 1; tc <= test_count; ++tc) {
        int dist[8];
        for (int i = 0; i < 4; ++i) {
            cin >> dist[i];
        }

        // Count number of numbers strictly greater than the first input.
        int result = 0;
        int a = dist[0];
        for (int i = 1; i < 4; ++i) {
            if (dist[i] > a) {
                ++result;
            }
        }

        cout << result << '\n';
    }

    return 0;
}
