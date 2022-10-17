/*
Solution to Problem H (Hopeless Bingo) from ICPC 2022 South Pacific Divisional
Finals (Level B).

Here, a number on a card is marked off by setting the number to -1.
*/



#include <bits/stdc++.h>


#define int_vec std::vector<long long>
#define int_mat std::vector<std::vector<long long>>
#define bool_vec std::vector<bool>
#define int long long
#define str_vec std::vector<std::string>
#define str std::string

using namespace std;


// Checks if a particular card in its current state has won.
bool is_winner(int_vec card) {
    for (int val : card) {
        if (val != -1) {
            return false;
        }
    }
    return true;
}


// Checks if a value is on a card.
bool is_member(int_vec card, int val) {
    for (int v : card) {
        if (v == val) {
            return true;
        }
    }
    return false;
}


// Check if a card is hopeless. If any value on the card is not in the set of
// tokens, it is hopeless.
bool is_hopeless(int_vec card, int_vec tokens) {
    for (int val : card) {
        if (!is_member(tokens, val)) {
            return true;
        }
    }
    return false;
}


// Marks off a single value on a card.
void mark_off(int_vec &card, int val) {
    for (size_t index = 0; index < card.size(); ++index) {
        if (card[index] == val) {
            card[index] = -1;
        }
    }
}


// Debugging function that prints an integer vector.
void print_vec(int_vec v) {
    for (int i : v) {
        cout << i << ' ';
    }
    cout << "\n";
}


// Debugging function that prints the current game status.
void print_game_status(int_mat game) {
    for (int_vec v : game) {
        print_vec(v);
    }
}



signed main(void) {
    // Read number of tokens, number of players, and number of values on each
    // card.
    int token_count, player_count, value_count;
    cin >> token_count >> player_count >> value_count;

    // Read value of each token.
    int_vec token_draws;
    token_draws.reserve(token_count);

    for (int i = 0; i < token_count; ++i) {
        int draw_value;
        cin >> draw_value;
        token_draws.push_back(draw_value);
    }

    // Set up player cards.
    str_vec card_statuses;
    int_mat player_cards;
    player_cards.reserve(player_count);
    for (int i = 0; i < player_count; ++i) {
        player_cards.push_back({});
        card_statuses.push_back("NULL");
    }

    for (int i = 0; i < player_count; ++i) {
        for (int j = 0; j < value_count; ++j) {
            int value;
            cin >> value;
            player_cards[i].push_back(value);
        }
    }

    // Filter out hopeless cards.
    for (int i = 0; i < player_count; ++i) {
        if (is_hopeless(player_cards[i], token_draws)) {
            card_statuses[i] = "hopeless";
        }
    }

    // Simulate the game. Draw each token one by one.
    bool winner_exists = false;
    for (int token : token_draws) {
        // Mark off the drawn token on each card.
        for (int_vec &card : player_cards) {
            mark_off(card, token);
        }

        // Determine if a winner has been found.
        for (int_vec card : player_cards) {
            if (is_winner(card)) {
                winner_exists = true;
                break;
            }
        }

        // Winner exists. Determine the status of all non-hopeless cards and
        // stop the simulation.
        if (winner_exists) {
            for (int index = 0; index < player_count; ++index) {
                if (is_winner(player_cards[index])) {
                    card_statuses[index] = "winning";
                } else if (card_statuses[index] != "hopeless") {
                    card_statuses[index] = "losing";
                }
            }
            break;
        }
    }

    // Print each card status.
    for (str val : card_statuses) {
        cout << val << "\n";
    }
}
