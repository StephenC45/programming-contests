/*
Solution to Problem A (Jelly Beans) from the 2022 New Zealand Programming 
Contest (ANZAC 6).

Problem was worth 3 points.
*/



#include <bits/stdc++.h>

#define int long long
#define int_vec std::vector<long long>
#define str_vec std::vector<std::string>

using namespace std;



signed main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Read actual number of jelly beans and number of guesses being made.
    int actual;
    cin >> actual;

    int guess_count;
    cin >> guess_count;

    // Store names, their guess, and the difference between the guess.
    str_vec names;
    names.reserve(guess_count);
    int_vec guesses;
    guesses.reserve(guess_count);
    int_vec diff;
    diff.reserve(guess_count);

    int min_diff = 99999999999999;

    // Read names, guesses, calculate difference, and update min_diff.
    for (int i = 0; i < guess_count; ++i) {
        string name;
        cin >> name;
        names.push_back(name);

        int guess;
        cin >> guess;
        guesses.push_back(guess);

        int guess_diff = abs(guess - actual);
        diff.push_back(guess_diff);

        if (guess_diff < min_diff) {
            min_diff = guess_diff;
        }
    }

    // Print name of first person to have guess with minimum difference from
    // correct answer.
    for (size_t index = 0; index < diff.size(); ++index) {
        if (diff[index] == min_diff) {
            cout << names[index] << "\n";
            break;
        }
    }

    return 0;
}
