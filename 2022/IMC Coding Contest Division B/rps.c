/*
Full solution to the RPS Round Robin problem from the 2022 IMC x CSESoc x CPMSoc
Coding Contest Division B.
*/



#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);

int parse_int(char*);

/*
 * Complete the 'solve' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER N
 *  2. STRING S
 */

int solve(int N, char* S) {

    int solution = 0;
    
    char robot_move[1];
    
    for (int i = 0; i < N; i++) {
        if (i % 3 == 0) {
            robot_move[0] = 'R';
        } else if (i % 3 == 1) {
            robot_move[0] = 'P';
        } else if (i % 3 == 2) {
            robot_move[0] = 'S';
        }
        
        if ((S[i] == 'R' && robot_move[0] == 'S') || (S[i] == 'S' && robot_move[0] == 'P') || (S[i] == 'P' && robot_move[0] == 'R')) {
            solution += (i + 1);
        }
        
        // printf("%s\n", robot_move);
    }
    
    return solution;

}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    /*
     * *********************************************************************
     * *                                                                   *
     * *   Everything from here handles input/output, and may be ignored.  *
     * *                                                                   *
     * *********************************************************************
     */

    int N = parse_int(ltrim(rtrim(readline())));

    char* S = readline();

    int result = solve(N, S);

    fprintf(fptr, "%d\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';

            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);

        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    while (*str != '\0' && isspace(*str)) {
        str++;
    }

    return str;
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }

    if (!*str) {
        return str;
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {
        end--;
    }

    *(end + 1) = '\0';

    return str;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);

    if (endptr == str || *endptr != '\0') {
        exit(EXIT_FAILURE);
    }

    return value;
}
