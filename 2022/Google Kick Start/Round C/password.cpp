/*
Full solution to the New Password problem from Google Kick Start 2022 Round C.

Loops over each password to check if it's valid, and if it's invalid, appends
a lowercase letter, uppercase letter, number, or special character if necessary.

If after appending the above, the password is still too short, appends zeroes.
*/



#include <bits/stdc++.h>

using namespace std;


// Functions that needlessly reinvent the wheel...
bool is_upper(char c) { // Should've used built-in isupper() function.
    return (c >= 'A' && c <= 'Z');
}

bool is_lower(char c) { // Should've used built-in isloweer() function.
    return (c >= 'a' && c <= 'z');
}

bool is_number(char c) { // Should've used built-in isdigit() function.
    return (c >= '0' && c <= '9');
}

bool is_special(char c) {
    return (c == '#' || c == '*' || c == '@' || c == '&');
}



int main(void) {
    int test_count;
    cin >> test_count;

    // Process all test cases.
    for (int i = 1; i <= test_count; ++i) {
        bool has_upper = false;
        bool has_lower = false;
        bool has_number = false;
        bool has_special = false;

        // Read and store old password, new password, and the password's length.
        string old_password;
        string new_password;
        int length;

        cin >> length;
        cin >> old_password;
        new_password = old_password;

        // Check if the password meets the uppercase, lowercase, digit, and
        // special character requirements.
        for (int index = 0; index < length; ++index) {
            if (is_upper(old_password[index])) {
                has_upper = true;
            }
            else if (is_lower(old_password[index])) {
                has_lower = true;
            }
            else if (is_number(old_password[index])) {
                has_number = true;
            }
            else if (is_special(old_password[index])) {
                has_special = true;
            }
        }

        // Add new characters if necessary.
        if (!has_upper) {
            new_password += 'A';
            ++length;
        }
        if (!has_lower) {
            new_password += 'a';
            ++length;
        }
        if (!has_number) {
            new_password += '1';
            ++length;
        }
        if (!has_special) {
            new_password += '@';
            ++length;
        }

        // Append enough zeroes to make the password long enough.
        while (length < 7) {
            new_password += '0';
            ++length;
        }

        // Print a line of output with a possible new password.
        cout << "Case #" << i << ": " << new_password << endl;
    }

    return 0;
}
