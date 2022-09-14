/*
Solution to problem M (Mixtape Managemnet) from 2022 ANZAC 5.
*/



#include <bits/stdc++.h>

using namespace std;

#define int long long
#define int_vec std::vector<int>


// Convert a positive integer to string.
string int_to_string(int n) {
    string result = "";
    // Add units digit to string, divide by 10 and discard remainder.
    while (n > 0) {
        int digit = n % 10;
        char new_ch = digit + '0';
        result += new_ch;
        n /= 10;
    }

    // Reverse the string.
    string result_tmp = result;
    result = "";
    for (int index = result_tmp.size() - 1; index >= 0; --index) {
        result += result_tmp[index];
    }

    return result;
}



int32_t main(void) {
    // Read number of items in permutatation, which is same as track count.
    int track_count;
    cin >> track_count;

    // Store track positions (numbers in the permutation) in a vector.
    int_vec track_positions;
    track_positions.reserve(track_count);

    for (int i = 0; i < track_count; ++i) {
        int track_pos;
        cin >> track_pos;
        track_positions.push_back(track_pos);
    }

    // Rename tracks to have a 3-digit count followed by 1's.
    for (size_t index = 0; index < track_positions.size(); ++index) {
        int count = 111 + index;
        string output = int_to_string(count);

        for (int i = 0; i < track_positions[index]; ++i) {
            output += "1";
        }

        // Print space-separated names.
        cout << output << " ";
    }
    cout << "\n";
    return 0;
}
