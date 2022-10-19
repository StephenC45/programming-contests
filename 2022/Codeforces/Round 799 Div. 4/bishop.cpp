/*
Solution to Problem C (Where's the Bishop?) from Codeforces Round 799 Division 
4.

More efficient solutions exist but input size is small enough that it is still
fine to search the entire chessboard.
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
        // Set up the chessboard.
        char chessboard[8][8];
        for (int i = 0; i < 8; ++i) {
            for (int j = 0; j < 8; ++j) {
                cin >> chessboard[i][j];
            }
        }

        // Search over the entire chessboard to find where the diagonal lines 
        // made by '#' characters intersect.
        int b_row = 0;
        int b_col = 0;
        for (int row = 1; row <= 6; ++row) {
            for (int col = 1; col <= 6; ++col) {
                if (chessboard[row][col] == '#') {
                    if (chessboard[row - 1][col - 1] == '#'
                    && chessboard[row - 1][col + 1] == '#'
                    && chessboard[row + 1][col - 1] == '#'
                    && chessboard[row + 1][col + 1] == '#') {
                        b_row = row + 1;
                        b_col = col + 1;
                        break;
                    }
                }
            }
        }

        cout << b_row << ' ' << b_col << '\n';
    }

    return 0;
}
