/*
Partially correct solution to Triktok from the 2023 IMC x CSESoc x CPMSoc 
Coding Competition Advanced Division.

Passed 11 out of 16 test cases for 64.29 out of 100 points.
*/



#include <bits/stdc++.h>


using namespace std;
#define int long long
#define int_v vector<int>

signed main(void) {
    // Read number of videos and store their lengths in a vector.
    int videos;
    cin >> videos;
    int_v lengths;
    lengths.reserve(videos);

    for (int i = 0; i < videos; ++i) {
        int duration;
        cin >> duration;
        lengths.push_back(duration);
    }

    // Take the duration modulo 3 of each video.
    int_v moduli;
    moduli.reserve(videos);
    int viral = 0;

    for (int i = 0; i < videos; ++i) {
        if (lengths[i] % 3 == 0) {
            ++viral;
        } else {
            moduli.push_back(lengths[i] % 3);
        }
    }

    // This is where it went wrong. The videos should have been put into buckets 
    // based on their duration modulo 3 to solve the problem.
    int sum = 0;
    for (size_t i = 0; i < moduli.size(); ++i) {
        sum += moduli[i];
        if (sum % 3 == 0) {
            sum -= 3;
            ++viral;
        }
    }

    cout << viral << "\n";
}
