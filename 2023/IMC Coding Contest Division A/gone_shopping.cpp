/*
Partially correct solution to the Gone Shopping problem from the 2023 IMC x 
CSESoc x CPMSoc Coding Competition Advanced Division.

Passed 7 out of 8 test cases for 80 out of 100 points.

This solution missed the edge case where there were n of one item, and one of 
another item.
*/



#include <bits/stdc++.h>


using namespace std;
#define int long long
#define str_int_map unordered_map<string, int>


signed main(void) {
    // Have an unordered_map<string, int> storing each item's name and the 
    // quantity purchased.
    str_int_map shop_list;

    int n_items;
    cin >> n_items;

    int unique_items = 0;
    for (int i = 0; i < n_items; ++i) {
        string item;
        cin >> item;
        if (shop_list.find(item) != shop_list.end()) {
            ++shop_list[item];
        } else {
            shop_list.emplace(item, 1);
            ++unique_items;
        }
    }

    // Calculate the total number of items purchased.
    int total_items = 0;
    for (auto [key, val] : shop_list) {
        total_items += val;
    }
    
    // Find the average number of items purchased and the irregular item (the 
    // item that needs to be removed).
    int average_items = total_items / unique_items;

    bool irregularity = false;
    string irregular_item = "";
    for (auto [key, val] : shop_list) {
        if (val != average_items && !irregularity) {
            irregularity = true;
            irregular_item = key;
        }

        else if (val != average_items && irregularity) {
            // There is a second irregularity, so it is impossible to remove 
            // exactly one item to make all items appear the same number of 
            // times.
            std::cout << "none\n";
            return 0;
        }
    }

    // No irregularity found, so all items appear the same number of times.
    if (irregular_item == "") {
        cout << "none\n";
        return 0;
    }

    // Irregularity found.
    cout << irregular_item << "\n";
    return 0;
}
