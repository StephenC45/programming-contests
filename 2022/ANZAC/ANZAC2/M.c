/* 
Unsubmitted attempt at Problem M (Ticket Completed?) from 2022 ANZAC 2.

Since this was never submitted, it is unknown whether this is correct. This 
program also does not free allocated memory.

The cities and rail links between them can be seen as a graph. However, an
adjacency matrix for 10 ^ 5 vertices would take up O((10 ^ 5) ^ 2) space and
would therefore exceed the memory limit. Thus, an adjacency list representation
of this graph must be used instead.

To find the number of possible tickets, it is simply the number of edges in the
complete graph.

To find the number of tickets where you will earn points, you must perform a
graph traversal (DFS or BFS) on each connected component to count the number
of vertices in each connected component.

For each connected component, there are (n * (n - 1)) / 2 possible tickets that
can be completed, where n is the number of vertices in that component. Total
up all of these values, and divide by the number of possible tickets to get
the solution.
*/



#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


// Adjacency lists are stored using linked lists.
typedef struct adj_list {
    int end_vertex;
    struct adj_list *next;
    struct adj_list *tail; // Pointer to tail of list.
} *adj_l;

// Adjacency list implementation - with 100000 vertices, an adjacency matrix
// would exceed the memory limit.
typedef struct Graph {
    int number_vertices; // Same as number of cities.
    adj_l *adj_lists;    // Array of pointers to adj_list.
} *Graph;



// Prints the graph to stdout for debugging.
void print_graph(Graph g) {
    for (int i = 0; i < g->number_vertices; i++) {
        printf("%d:  ", i); // Print vertex number.
        for (adj_l curr = g->adj_lists[i]; curr != NULL; curr = curr->next) {
            printf("%d ", curr->end_vertex); // Print each end vertex.
        }
        printf("\n");
    }
}

// Prints graph to stdout for debugging, but only prints vertices that have
// outgoing edges.
void print_graph_some(Graph g) {
    for (int i = 0; i < g->number_vertices; i++) {
        if (g->adj_lists[i] == NULL) {
            continue; // Skip vertices with no outgoing edges.
        }
        
        printf("%d:  ", i); // Print vertex number.
        for (adj_l curr = g->adj_lists[i]; curr != NULL; curr = curr->next) {
            printf("%d ", curr->end_vertex); // Print each end vertex.
        }
        printf("\n");
    }
}

// Recursively uses depth-first search to count number of nodes reachable in one 
// connected component, starting from the vertex start_v.
int DFS(Graph g, int start_v, int *visit) {
    // Mark start vertex as visited.
    visit[start_v] = 1;
    int count = 0;
    //printf("Doing DFS from node %d\n", start_v);

    // Fetch and iterate over the adjacency list.
    adj_l outlinks = g->adj_lists[start_v];
    for (adj_l curr = outlinks; curr != NULL; curr = curr->next) {
        //printf("Vertex found from %d to %d\n", start_v, curr->end_vertex);

        if (visit[curr->end_vertex] == 0) {
            // End vertex not visited. Recursive call wiil mark it as visited.
            // Add number of reachable nodes from next vertex to current count.
            int reachable = DFS(g, curr->end_vertex, visit);
            count += reachable;
        }
    }

    // Add one for current node or start vertex.
    count += 1;
    return count;
}

// Appends to an adjacency list in O(1) time.
adj_l insert_into_list(adj_l list, int n) {
    // Create new node, set its next to NULL, and set end_vertex to n.
    adj_l new = malloc(sizeof(struct adj_list));
    new->next = NULL;
    new->end_vertex = n;

    if (list == NULL) {
        // List is empty.
        list = new;
        list->tail = new;
        return list;
    }
    
    list->tail->next = new;
    list->tail = new; // Modify the tail of the original list.

    return list;
}

// Creates a new graph.
Graph new_graph(int n) {
    // Malloc for graph itself.
    Graph new = malloc(sizeof(struct Graph));
    assert(new != NULL); // Checking that malloc succeeded. Good practice.

    new->number_vertices = n;

    // Malloc an array of pointers to adjacency lists.
    new->adj_lists = malloc(n * sizeof(adj_l));
    assert(new->adj_lists != NULL);

    // Initialise all adjacency lists to empty.
    for (int i = 0; i < n; i++) {
        new->adj_lists[i] = NULL;
    }

    return new;
}

// Inserts an edge into a graph in O(1) time.
Graph insert_edge(Graph g, int start_v, int end_v) {
    g->adj_lists[start_v] = insert_into_list(g->adj_lists[start_v], end_v);
    return g;
}



int main(void) {
    double number_of_cities; // Number of cities.
    double claimed_links;    // Number of rail links you have already claimed.
    double valid_paths = 0;  // Number of paths that result in completion.
    
    // Read the input.
    scanf("%lf %lf", &number_of_cities, &claimed_links);

    // Create graph and visited array.
    Graph network = new_graph(number_of_cities);
    int *visited = calloc(number_of_cities, sizeof(int));

    // Insert claimed rail links as edges into graph.
    for (int i = 0; i < claimed_links; i++) {
        int start;
        int end;
        scanf("%d %d", &start, &end);
        network = insert_edge(network, start - 1, end - 1);
    }

    // Perform DFS on each connected component.
    for (int index = 0; index < number_of_cities; index++) {
        if (visited[index] == 0) {
            double reachable_nodes = DFS(network, index, visited);
            valid_paths += (reachable_nodes * (reachable_nodes - 1)) / 2;
        }
    }

    // Number of possible links or tickets is the number of edges in a
    // complete graph with number_of_cities vertices.
    double possible_links = (number_of_cities * (number_of_cities - 1)) / 2;
    //printf("%lf possible links\n", possible_links);

    // Print the probability that out of any possible link, the random ticket
    // you get will earn you points.
    printf("%lf\n", valid_paths / possible_links);
}