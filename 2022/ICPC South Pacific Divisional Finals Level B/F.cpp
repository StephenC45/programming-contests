/*
Solution to Problem F (Falling Domi ...no, no, NOO!) from ICPC 2022 South 
Pacific Divisional Finals (Level B).

This was solved by me but implemented by my teammates.

The dominoes can be represented as a directed graph and we can DFS on all
dominoes to find the chaos factor.
*/



#include <bits/stdc++.h>


// Due to small input size, an adjacency matrix where DFS is O(n^2) is still
// efficient enough. The overall time complexity is therefore O(n^3) with n
// dominoes.
int adj[105][105];
int visited[105];  // Visited nodes.


// Depth-first search that returns a count of reachable nodes.
int dfs(int src, int d) {
    // Reset visited nodes array.
    for (int i = 0; i < d + 5; i++) {
        visited[i] = 0;
    }

    std::stack<int> stack; // DFS stack.
    stack.push(src);

    while(!stack.empty()) {
        int node = stack.top();
        stack.pop();

        if (visited[node]) continue; // Skip nodes that are already visited.

        visited[node] = 1; // Mark the current node as visited.

        for (int i = 1; i <= d; i++) {
            if (i == node) continue; // Skip case where node is itself.

            // If the current node and node i are adjacent, push onto DFS stack.
            if (adj[node][i] == 1) {
                stack.push(i);
            }
        }
    }

    // Count the number of visited nodes. This could have been moved into the
    // main DFS loop but it still works.
    int count = 0;
    for (int i = 1; i <= d; i++) {
        if (visited[i] == 1) {
            count++;
        }
    }

    return count;
}



int main(void) {
    // Read number of dominoes and relations between the dominoes.
    int d, r;
    std::cin >> d >> r;

    for (int i = 0; i < r; i++) {
        int from, to;
        std::cin >> from >> to;
        adj[from][to] = 1;
    }

    // Call DFS on each domino and print the chaos factors space-separated.
    for (int i = 0; i < d; i++) {
        std::cout << dfs(i + 1, d) << ' ';
    }
    std::cout << '\n';

    return 0;
}
