/*
Full and very heavily commented solution to the Rigged Election problem.
https://www.hackerrank.com/contests/2022-annual-programming-competition-division-b/challenges/rigged-election

Scored 10 points.
*/



// A nice trick for competitive progammming. However, it increases compilation
// time dramatically.
#include <bits/stdc++.h>

using namespace std; // Don't do this outside of programming contests.

// A vector is a better version of C arrays, this #define provides a shorthand.
// Insertion in amortised O(1) time.
// Can grow dynamically.
#define int_vec std::vector<int>


// Debugging function. Prints all integers in vector v with a for-range loop.
void print_vector(int_vec v) {
    for (int val : v) {
        cout << val << " ";
    }
    cout << "\n";
}



int main(void) {
    // Read N and M.
    int N, M;
    cin >> N >> M;

    // vote_arr wan't really needed.
    // vote_counts stores vote counts for each candidate. Candidate i has
    // vote_counts[i] votes for them.
    int_vec vote_arr;
    int_vec vote_counts;

    // Zero initialise everyone's votes. Be careful of one-based indexing in the
    // problem when C++ vectors are zero-based.
    for (int i = 0; i < M + 1; ++i) {
        vote_counts.push_back(0);
    }

    // Read in the candidate person i voted for and update vote counts.
    for (int i = 0; i < N; ++i) {
        int candidate;
        cin >> candidate;
        ++vote_counts[candidate];
    }

    // Store maximum value and index of maximum value.
    int max = -1;
    size_t max_index = -1;
    for (size_t index = 0; index < vote_counts.size(); ++index) {
        if (vote_counts[index] > max) {
            max = vote_counts[index];
            max_index = index;
        }
    }

    // Print 1 if candidate 1 has most votes and there is another candidate also
    // with the most votes.
    for (size_t index = 2; index < vote_counts.size(); ++index) {
        if (vote_counts[index] == max && max_index != index) {
            cout << "1\n";
            return 0;
        }
    }

    if (max == vote_counts[1]) {
        // Candidate 1 already has the most votes and no other candidate is tied
        // with them.   
        cout << 0 << "\n";
    } else {
        // Candidate 1 does not have the most number of votes.
        cout << max - vote_counts[1] + 1 << "\n";
    }
}
