/*
Solution to Problem K (Kiwis, Snakes, and Ladders) from ICPC 2022 South Pacific
Divisional Finals (Level B). 

This was solved and implemented by my teammates.
*/



#include <bits/stdc++.h>

// Board, player positions, cards, and whether the player is losing a turn or
// not are all stored in these global variables.
int board[120];
int players[4];
int skips[4];
int cards[105];


int main(void) {
    // Set up the board as a one-dimensional array.
    for (int row = 0; row < 10; row++) {
        for (int col = 0; col < 10; col++) {
            int polarity = (row % 2 == 0) ? -1 : 1;
            int shift = (polarity == 1) ? 9 : 0;
            
            int offset = 100 - row * 10 + polarity * col - shift;
            std::cin >> board[offset];
        }
    }

    // Set up the cards that will be drawn.
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> cards[i];
    }

    // Initialise each player's position as (square) 1.
    for (int i = 0; i < 4; i++) {
        players[i] = 1;
    }

    int draw = 0;   // Number of cards drawn.
    int player = 0; // Number of current player (0 to 3).
    int done = 0;   // Number of players that have finished.
    while (draw < n) {
        if (done == 4) break; // Stop drawing cards when all players finished.

        if (skips[player] == 1) {
            // Player has lost this turn.
            skips[player] = 0;
            player = (player + 1) % 4;
            continue;
        }
        if (players[player] == 101) {
            // Player has finished.
            player = (player + 1) % 4;
            continue;
        }
        
        // Get value on the current card and move the player forward.
        int card = cards[draw];
        players[player] += card;
        
        int pos = players[player];
        if (pos > 100) {
            // Player has finished.
            players[player] = 101;
            done++;
        }

        if (board[pos] == -1) {
            // Player landed on a kiwi, loses their next turn.
            skips[player] = 1;
        }
        if (board[pos] > 0) {
            // Player landed on a snake or ladder, teleport to corresponding
            // location.
            players[player] = board[pos];
        }
        
        // Go to next player and increment number of cards drawn.
        player = (player + 1) % 4;
        draw++;
    }

    // Print the location of each player, space separated.
    for (int i = 0; i < 4; i++) {
        std::cout << players[i] << " ";
    }
    std::cout << '\n';
    return 0;
}
