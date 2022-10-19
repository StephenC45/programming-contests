/*
Solution to Problem B (All Distinct) from Codeforces Round 799 Division 4.
*/



#include <bits/stdc++.h>

using namespace std; // Please don't do this outside of programming contests...



// Returns true if the given integer is in a vector.
bool is_member(vector<int> in_vec, int search) {
    for (long unsigned int index = 0; index < in_vec.size(); ++index) {
        if (in_vec[index] == search) {
            return true;
        }
    }
    return false;
}



int32_t main(void) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    // Read the number of test cases.
    int test_count;
    cin >> test_count;

    // Process each test case.
    for (int tc = 1; tc <= test_count; ++tc) {
        int array[55];
        int size;
        cin >> size;

        for (int i = 0; i < size; ++i) {
            cin >> array[i];
        }

        // Create a vector of unique elements.
        vector<int> unique_elems;
        unique_elems.reserve(size);
        for (int index = 0; index < size; ++index) {
            if (!is_member(unique_elems, array[index])) {
                unique_elems.push_back(array[index]);
            }
        }

        // Count duplicates.
        int duplicate_count = 0;
        for (int slow = 0; slow < size; ++slow) {
            for (int fast = slow + 1; fast < size; ++fast) {
                if (array[slow] == array[fast]) {
                    ++duplicate_count;
                }
            }
        }

        // Determine number of operations needed.
        int u_size = unique_elems.size();
        int operation_count = (size - u_size) / 2;
        if ((size - u_size) & 1) {
            // Have to remove an odd number of elements.
            ++operation_count;
        }

        // Each operation removes 2 elements from the original array.
        int answer = size - (2 * operation_count);
        cout << answer << '\n';
    }

    return 0;
}
