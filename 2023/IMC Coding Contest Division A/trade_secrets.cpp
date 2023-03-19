/*
Full solution to the Trade Secrets problem from the 2023 IMC x CSESoc x CPMSoc 
Coding Competition Advanced Division.
*/



#include <bits/stdc++.h>


using namespace std;
#define int long long
#define int_v vector<int>


// Returns true if and only if a string is all digits.
bool is_all_digits(string s) {
    for (char c : s) {
        if (c < '0' || c > '9') {
            return false;
        }
    }
    return true;
}


// Returns true if and only if a string is all characters (a-z).
bool is_all_chars(string s) {
    for (char c : s) {
        if (c < 'a' || c > 'z') {
            return false;
        } 
    }
    return true;
}


// Calculates the value of the given stock name.
int calculate_value(string s) {
    if (is_all_digits(s)) {
        // All digits.
        int val = 0;
        for (char c : s) {
            val += c - '0';
        }

        return val;
    } else if (is_all_chars(s)) {
        // All chars.
        int val = 0;
        for (char c : s) {
            val += c - 'a' + 1;
        }

        return val;
    } else {
        // Mix of digits and chars.
        return s.length();
    }
}


signed main(void) {
    int n_names;
    cin >> n_names;

    // This problem is quite simple, especially when there is only one stock 
    // with maximum value.
    int max_value = -1;
    string best_stock = "";

    for (int i = 0; i < n_names; ++i) {
        string stock_name;
        cin >> stock_name;

        int val = calculate_value(stock_name);
        if (val > max_value) {
            best_stock = stock_name;
            max_value = val;
        }
    }

    std::cout << best_stock << "\n";
}
