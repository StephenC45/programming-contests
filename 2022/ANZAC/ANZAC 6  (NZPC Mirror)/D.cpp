/*
Solution to Problem D (Winning the Toss) from the 2022 New Zealand Programming
Contest (ANZAC 6).

Problem was worth 3 points.
*/



#include <bits/stdc++.h>

#define int long long
#define int_vec std::vector<long long>
#define str_vec std::vector<std::string>

using namespace std;



signed main(void) {
    // Read number of games.
    int game_count;
    cin >> game_count;

    for (int i = 0; i < game_count; ++i) {
        // Colours determined by first integer and whether or not they won the
        // toss.
        int colour;
        cin >> colour;

        string required;
        cin >> required;

        string actual;
        cin >> actual;

        if (colour == 1) {
            if (required == actual) {
                // Won the toss.
                cout << "blue and black\n";
            } else {
                // Lost the toss.
                cout << "red and yellow\n";
            }
        } else {
            if (required == actual) {
                // Won the toss.
                cout << "green and brown\n";
            } else {
                // Lost the toss.
                cout << "pink and white\n";
            }
        }
    }

    return 0;
}
