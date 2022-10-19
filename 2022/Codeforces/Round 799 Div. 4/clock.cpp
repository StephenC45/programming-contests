/*
Solution to Problem D (The Clock) from Codeforces Round 799 Division 4.
*/



//#include <bits/stdc++.h> Commented out for faster compilation time.
#include <iostream>

#define int long long
#define HOURS_MOD 24
#define MINUTES_MOD 60

using namespace std;



// Converts a time to a string.
string time_to_str(int hour, int minute) {
    string hour_p = "";
    if (hour < 10) {
        hour_p += "0";
    }

    string minute_p = "";
    if (minute < 10) {
        minute_p += "0";
    }
    
    hour_p += to_string(hour);
    minute_p += to_string(minute);

    return hour_p + ":" + minute_p;
}


// Prints the current time.
void print_time(int h, int m) {
    cout << time_to_str(h, m) << '\n';
    return;
}


// Adds hours and minutes to the current time.
void add_time(int &curr_h, int &curr_m, int &h_diff, int &m_diff) {
    int m_sum = curr_m + m_diff;
    while (m_sum >= MINUTES_MOD) {
        ++curr_h;
        m_sum -= MINUTES_MOD;
    }

    int h_sum = curr_h + h_diff;
    while (h_sum >= HOURS_MOD) {
        h_sum -= HOURS_MOD;
    }

    curr_h = h_sum;
    curr_m = m_sum;

    return;
}


// Returns true if the input string is a palindrome.
bool is_palindrome(string input) {
    string reversed = "";
    for (int index = input.size() - 1; index >= 0; --index) {
        reversed += input[index];
    }

    return (reversed == input);
}



int32_t main(void) {
    /* Still passed within the time limit despite having this commented out.
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    */
    
    // Read the number of test cases.
    int test_count;
    cin >> test_count;

    // Process each test case.
    for (int tc = 1; tc <= test_count; ++tc) {
        string input;
        int interval;
        cin >> input >> interval;
        
        // Determine the starting time.
        int start_h = 10 * (input[0] - '0') + (input[1] - '0');
        int start_m = 10 * (input[3] - '0') + (input[4] - '0');

        int curr_h = start_h;
        int curr_m = start_m;

        // Determine the number of hours and minutes on each interval.
        int h_diff = interval / 60;
        int m_diff = interval % 60;

        // Check if start time is a palindrome.
        int palindromes = 0;
        if (is_palindrome(time_to_str(start_h, start_m))) {
            ++palindromes;
        }

        // Count palindromes seen until same start hour and start minute.
        add_time(curr_h, curr_m, h_diff, m_diff);
        while (curr_h != start_h || curr_m != start_m) {
            if (is_palindrome(time_to_str(curr_h, curr_m))) {
                ++palindromes;
            }
            add_time(curr_h, curr_m, h_diff, m_diff);
        }

        cout << palindromes << "\n";
    }

    return 0;
}
