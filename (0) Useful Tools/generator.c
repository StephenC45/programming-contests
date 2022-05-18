/*
Input generator that creates a file 'input.txt' containing the generated input.
*/



// Include header files here.
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// All #defines here.
#define MOD_CONST 1000000



int main(void) {
    // Seed random number generator.
    srand(time(0));
    
    printf("Starting input generator...\n\n");
    FILE *input = fopen("input.txt", "w");

    long long input_size;
    printf("Enter input size: ");
    scanf("%lld", &input_size);

    for (long long i= 1; i <= input_size; ++i) {
        fprintf(input, "%lld", rand() % MOD_CONST);
    }
}
