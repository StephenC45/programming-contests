/*
Solution to Problem F (Battleships) from 2022 New Zealand Programming Contest 
(ANZAC 6).

Problem was worth 10 points but can be surprisingly difficult. Took 5 tries to
get it right because my initial approach broke on coordinates ending with '10' 
and had problems adding diagonal objects to the grid.

The playing grid is represented by a 2D integer array.
*/



#include <bits/stdc++.h>

#define int long long
#define int_vec std::vector<long long>
#define int_mat std::vector<std::vector<long long>>

#define BATTLESHIP_H 11
#define BATTLESHIP_V 12
#define BATTLESHIP_D 13

#define DESTROYER_H 21
#define DESTROYER_V 22
#define DESTROYER_D 23

#define CRUISER_H 31
#define CRUISER_V 32
#define CRUISER_D 33

#define SUBMARINE_H 41
#define SUBMARINE_V 42
#define SUBMARINE_D 43


using namespace std;


// Debugging function that prints an integer matrix.
void print_matrix(int_mat m);


// Adds an item to the playing grid.
void add_item(int_mat &m, string type, int r1, int r2, int c1, int c2);


// Calculates the distance between two coordinates.
int calculate_length(int r1, int r2, int c1, int c2);


// Swaps two numbers.
void swap(int &n1, int &n2);


// Adds a diagonal item to the playing grid.
void add_diagonal_item(int_mat &m, int type, int r1, int r2, int c1, int c2);



signed main(void) {
    // Set up playing grid, set all values to -1 initially.
    int_mat playgrid;
    playgrid.reserve(10);
    for (int i = 0; i < 10; ++i) {
        playgrid.push_back({});
        for (int j = 0; j < 10; ++j) {
            playgrid[i].push_back(-1);
        }
    }
    
    // Read the start and end coordinates of the 4 items that comprise the 
    // fleet and add them to the grid.
    for (int i = 0; i < 4; ++i) {
        // Read the start and end coordinates separately.
        string coord1;
        cin >> coord1;

        string coord2;
        cin >> coord2;

        int row1, row2, col1, col2;

        if (coord1.length() == 3) {
            // Coordinate ends with '10' instead of a single digit.
            row1 = 9;
        } else {
            row1 = coord1[1] - '0' - 1;
        }

        if (coord2.length() == 3) {
            // Coordinate ends with '10' instead of a single digit.
            row2 = 9;
        } else {
            row2 = coord2[1] - '0' - 1;
        }

        col1 = coord1[0] - 'A';
        col2 = coord2[0] - 'A';
        
        if (col1 > col2 && row1 > row2) {
            swap(col1, col2);
            swap(row1, row2);
        }

        // Calculate length of the item before deciding what to add.
        int length = calculate_length(row1, row2, col1, col2);

        if (length == 5) {
            add_item(playgrid, "battleship", row1, row2, col1, col2);
        } else if (length == 4) {
            add_item(playgrid, "destroyer", row1, row2, col1, col2);
        } else if (length == 3) {
            add_item(playgrid, "cruiser", row1, row2, col1, col2);
        } else if (length == 2) {
            add_item(playgrid, "submarine", row1, row2, col1, col2);
        }
    }

    // Read in attacks until a "X0" is read.
    string attack;
    cin >> attack;
    while (attack != "X0") {
        int col = attack[0] - 'A';
        int row;
        if (attack.size() == 3) {
            row = 9;
        } else {
            row = attack[1] - '0' - 1;
        }
        
        // Print what happens as a result of the attack.
        if (playgrid[row][col] == BATTLESHIP_D) {
            cout << "Hit Battleship Diagonal\n";
        } else if (playgrid[row][col] == BATTLESHIP_H) {
            cout << "Hit Battleship Horizontal\n";
        } else if (playgrid[row][col] == BATTLESHIP_V) {
            cout << "Hit Battleship Vertical\n";
        } else if (playgrid[row][col] == DESTROYER_D) {
            cout << "Hit Destroyer Diagonal\n";
        } else if (playgrid[row][col] == DESTROYER_H) {
            cout << "Hit Destroyer Horizontal\n";
        } else if (playgrid[row][col] == DESTROYER_V) {
            cout << "Hit Destroyer Vertical\n";
        } else if (playgrid[row][col] == CRUISER_D) {
            cout << "Hit Cruiser Diagonal\n";
        } else if (playgrid[row][col] == CRUISER_H) {
            cout << "Hit Cruiser Horizontal\n";
        } else if (playgrid[row][col] == CRUISER_V) {
            cout << "Hit Cruiser Vertical\n";
        } else if (playgrid[row][col] == SUBMARINE_D) {
            cout << "Hit Submarine Diagonal\n";
        } else if (playgrid[row][col] == SUBMARINE_H) {
            cout << "Hit Submarine Horizontal\n";
        } else if (playgrid[row][col] == SUBMARINE_V) {
            cout << "Hit Submarine Vertical\n";
        } else {
            cout << "Miss\n";
        }

        cin >> attack;
    }
}



// Debugging function that prints an integer matrix.
void print_matrix(int_mat m) {
    for (size_t ind1 = 0; ind1 < m.size(); ++ind1) {
        for (int value : m[ind1]) {
            cout << value << "  ";
        }
        cout << "\n";
    }
    return;
}


// Adds an item to the playing grid.
void add_item(int_mat &m, string type, int r1, int r2, int c1, int c2) {
    int fleet_type = 0;

    if (type == "battleship") {
        if (r1 == r2) {
            fleet_type = BATTLESHIP_H;
            for (int i = c1; i <= c2; ++i) {
                m[r1][i] = fleet_type;
            }
        } else if (c1 == c2) {
            fleet_type = BATTLESHIP_V;
            for (int i = r1; i <= r2; ++i) {
                m[i][c1] = fleet_type;
            }
        } else {
            fleet_type = BATTLESHIP_D;
            add_diagonal_item(m, fleet_type, r1, r2, c1, c2);
        }

    } else if (type == "destroyer") {
        if (r1 == r2) {
            fleet_type = DESTROYER_H;
            for (int i = c1; i <= c2; ++i) {
                m[r1][i] = fleet_type;
            }
        } else if (c1 == c2) {
            fleet_type = DESTROYER_V;
            for (int i = r1; i <= r2; ++i) {
                m[i][c1] = fleet_type;
            }
        } else {
            fleet_type = DESTROYER_D;
            add_diagonal_item(m, fleet_type, r1, r2, c1, c2);
        }

    } else if (type == "cruiser") {
        if (r1 == r2) {
            fleet_type = CRUISER_H;
            for (int i = c1; i <= c2; ++i) {
                m[r1][i] = fleet_type;
            }
        } else if (c1 == c2) {
            fleet_type = CRUISER_V;
            for (int i = r1; i <= r2; ++i) {
                m[i][c1] = fleet_type;
            }
        } else {
            fleet_type = CRUISER_D;
            add_diagonal_item(m, fleet_type, r1, r2, c1, c2);
        }

    } else if (type == "submarine") {
        if (r1 == r2) {
            fleet_type = SUBMARINE_H;
            for (int i = c1; i <= c2; ++i) {
                m[r1][i] = fleet_type;
            }
        } else if (c1 == c2) {
            fleet_type = SUBMARINE_V;
            for (int i = r1; i <= r2; ++i) {
                m[i][c1] = fleet_type;
            }
        } else {
            fleet_type = SUBMARINE_D;
            add_diagonal_item(m, fleet_type, r1, r2, c1, c2);
        }
    }

    return;
}


// Calculates the distance between two coordinates.
int calculate_length(int r1, int r2, int c1, int c2) {
    // Return the difference in column or row.
    if (r1 == r2) {
        return abs(c2 - c1) + 1;
    } else {
        return abs(r2 - r1) + 1;
    }
}


// Swaps two numbers.
void swap(int &n1, int &n2) {
    int temp = n2;
    n2 = n1;
    n1 = temp;
    return;
}


// Adds a diagonal item to the playing grid.
void add_diagonal_item(int_mat &m, int type, int r1, int r2, int c1, int c2) {
    if (r1 > r2 && c1 > c2) {
        // Diagonal heading up and left.
        int i = r1;
        int j = c1;
        while (i >= r2) {
            m[i][j] = type;
            --i;
            --j;
        }
    } else if (r1 < r2 && c1 < c2) {
        // Diagonal heading down and right.
        int i = r1;
        int j = c1;
        while (i <= r2) {
            m[i][j] = type;
            ++i;
            ++j;
        }
    } else if (r1 < r2 && c1 > c2) {
        // Diagonal heading down and left.
        int i = r1;
        int j = c1;
        while (i <= r2) {
            m[i][j] = type;
            ++i;
            --j;
        }
    } else if (r1 > r2 && c1 < c2) {
        // Diagonal heading up and right.
        int i = r1;
        int j = c1;
        while (i >= r2) {
            m[i][j] = type;
            --i;
            ++j;
        }
    }

    return;
}
