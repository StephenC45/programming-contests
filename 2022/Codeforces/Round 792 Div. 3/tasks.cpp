/*
Submission for Problem C (Restoring the Duration of Tasks) from Codeforces
Round #797 Div. 3.

Accepted.
*/



#include <bits/stdc++.h>

using namespace std;

#define int_vec std::vector<int>


int32_t main(void) {
    // Make I/O faster.
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int test_count;
    cin >> test_count;

    for (int i = 1; i <= test_count; ++i) {
        int start_time = 0;
        
        // Read number of tasks.
        int tasks;
        cin >> tasks;

        int_vec given_times;    // Times that task i was given.
        int_vec start_times;    // Times that task i was started.
        int_vec finished_times; // Times that task i was finished.
        int_vec durats;         // Unused.

        // Read the times the tasks were given.
        for (int index= 0; index < tasks; ++index) {
            int time;
            cin >> time;
            if (index == 0) {
                start_time = time; // Record start time of first task.
            }
            
            // Fill vector storing times the tasks were given.
            given_times.push_back(time);
        }

        // Read the times the tasks were finished.
        for (int index= 0; index< tasks; ++index) {
            int time;
            cin >> time;
            finished_times.push_back(time);
        }

        // The start time of task i is the greater of the finish time of
        // task (i - 1) or the time task i was given.
        start_times.push_back(start_time);
        for (int index = 1; index < tasks; ++index) {
            start_times.push_back(max(finished_times[index - 1], given_times[index]));
        }

        // Print the durations of each task, space separated.
        for (int j = 0; j < tasks; ++j) {
            cout << finished_times[j] - start_times[j] << ' ';
        }
        cout << '\n';

    }

    return 0;
}
