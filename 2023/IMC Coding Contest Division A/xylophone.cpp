/*
Partially correct solution to the Xylophone problem from the 2023 IMC x CSESoc x 
CPMSoc Coding Competition Advanced Division.

Passed 15 out of 30 test cases for 50 out of 100 points.

This solution was naive.
*/



#include <bits/stdc++.h>


using namespace std;
#define int long long
#define int_bool_map unordered_map<int, bool>
#define int_set unordered_set<int>


signed main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int_set played_tones;

    int n_songs, common_gap, xylophone_length;
    cin >> n_songs>> common_gap >> xylophone_length;

    for (int i = 0; i < n_songs; ++i) {
        int start_tone,length;
        cin >> start_tone >> length;

        for (int j = 0; j < length; ++j) {
            played_tones.emplace(start_tone + common_gap * j);
        }
    }

    std::cout << played_tones.size() << "\n";
}
