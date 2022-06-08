/*
Submission for Problem A (Print a Pedestal (Codeforces Logo?)) from Codeforces
Round #797 Div. 3.

Accepted.
*/



#include <bits/stdc++.h>

using namespace std;

#define int long long


int32_t main(void) {
    // Make I/O faster.
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int test_count;
    cin >> test_count;

    for (int i = 1; i <= test_count; ++i) {
        // Read the number of blocks that need to be used.
        int block_count;
        cin >> block_count;

        // Find the minimum value of number of blocks used for 1st place, and 
        // the maximum number of blocks that can be used with this minimum.
        int min_first = block_count / 3;
        int blocks_used = min_first + min_first - 1 + min_first - 2;
        
        // Assign initial values for 1st, 2nd, and 3rd place, and find the
        // difference between the number of blocks used and the number of blocks
        // that need to be used.
        int difference = block_count - blocks_used;
        int first = min_first;  
        int second = first - 1; 
        int third = second - 1; 

        // Add blocks in a way to minimise the height of 1st place.
        while (difference > 0) {
            if (first > (second + 1)) {
                ++second;
            } else if (second > (third + 1)) {
                ++third;
            } else {
                ++first;
            }
            --difference;
        }

        // Print the pedestal.
        cout << second << " " << first << " " << third << '\n';
    }

    return 0;
}