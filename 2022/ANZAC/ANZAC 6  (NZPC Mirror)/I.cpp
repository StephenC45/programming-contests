/*
Solution to Problem I (Farmer Party) from 2022 New Zealand Programming Contest 
(ANZAC 6).

Problem was worth 30 points.

Input size is small enough for a brute force O(n^3) solution to pass within the
time limit.
*/



#include <bits/stdc++.h>

#define int long long
#define int_vec std::vector<long long>
#define str_vec std::vector<std::string>

using namespace std;


// Calculates total distance farmers need to travel if farmer i1 and i2 host.
int calculate_distances(int i1, int i2, int_vec distances);



signed main(void) {
    int farmer_count;
    cin >> farmer_count;

    // Store distance of each farmer from end of the road in a vector.
    int_vec distances;
    distances.reserve(farmer_count);

    for (int i = 0; i < farmer_count; ++i) {
        int dist;
        cin >> dist;
        distances.push_back(dist);
    }

    // If there are only 2 farmers, both can host and no travel is required.
    if (farmer_count == 2) {
        cout << "0\n";
        return 0;
    }

    int min_distance = 9999999999999;

    // Find the minimum distance for all pairs of farmers that can host.
    for (int index1 = 0; index1 < farmer_count; ++index1) {
        for (int index2 = index1 + 1; index2 < farmer_count; ++index2) {
            int distance = calculate_distances(index1, index2, distances);
            if (distance < min_distance) {
                min_distance = distance;
            }
        }
    }

    cout << min_distance << "\n";
    return 0;
}



// Calculates total distance farmers need to travel if farmer i1 and i2 host.
int calculate_distances(int i1, int i2, int_vec distances) {
    int size = distances.size();
    int distance_sum = 0;

    for (int index = 0; index < size; ++index) {
        // Take absolute value from farmer i1 and farmer i2.
        int dist1 = abs(distances[i1] - distances[index]);
        int dist2 = abs(distances[i2] - distances[index]);
        
        // Add the smaller of the two values.
        if (dist1 < dist2) {
            distance_sum += dist1;
        } else {
            distance_sum += dist2;
        }
    }

    // Multiply by 2 to account for return journey.
    return distance_sum << 1;
}
