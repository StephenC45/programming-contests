/*
Solution to Problem A (A Powerful Tower) from ICPC 2022 South Pacific Divisional
Finals (Level B).
*/



#include <bits/stdc++.h>


#define int long long
#define str std::string
#define str_vec std::vector<std::string>

using namespace std;


// Checks if a string has all its characters the same.
bool all_same_characters(str str1) {
    char check = str1[0];
    for (size_t i = 1; i < str1.length(); ++i) {
        if (str1[i] != check) {
            return false;
        }
    }
    return true;
}



signed main(void) {
    // Read number of rows and columns.
    int rows, columns;
    cin >> rows >> columns;

    str_vec input;
    input.reserve(rows);

    // Read each row.
    for (int i = 0; i < rows; ++i) {
        std::string inputstr;
        cin >> inputstr;
        input.push_back(inputstr);
    }

    str_vec column_strs;
    column_strs.reserve(columns);

    // Populate column_strs such that column_strs[i] is the same as the string
    // in column i from top to bottom.
    str column_str = "";
    for (int i = 0; i < columns; ++i) {
        column_str = "";
        for (int j = 0; j < rows; ++j) {
            column_str += input[j][i];
        }
        column_strs.push_back(column_str);
    }

    // Handle case where there is one row.
    if (rows == 1) {
        cout << columns << "\n";
        return 0;
    }

    // Calculate the longest run of consecutive columns where all characters
    // are the same in each column.
    int max_power = 0;
    int start_col = 0;
    int finish_col = 0;
    int curr_power = 0;
    bool started = false;
    for (int i = 0; i < columns; ++i) {
        if (all_same_characters(column_strs[i]) && !started) {
            // Mark off starting point.
            start_col = i;
            started = true;
        } else if (started && !all_same_characters(column_strs[i])) {
            // Mark off finishing point and calculate the power of this tower.
            // Also update the maximum power if needed.
            finish_col = i;
            curr_power = finish_col - start_col;
            if (curr_power > max_power) {
                max_power = curr_power;
            }
            started = false;
        } else if (started && i == columns - 1 && all_same_characters(column_strs[i])) {
            // The last column has all characters the same. Calculate the power
            // and update the maximum power if needed.
            finish_col = columns;
            curr_power = finish_col - start_col;
            if (curr_power > max_power) {
                max_power = curr_power;
            }
            started = false;
        }
    }

    cout << max_power << "\n";
}
