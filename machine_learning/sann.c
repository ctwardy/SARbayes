#include "data.h"


void simulated_annealing(table *data) {
    
}


int main(int argc, char **argv) {
    if(argc < 2) {
        printf("Usage: %s [filename]\n", argv[0]);
        return EXIT_FAILURE;
    }
    
    char *filename = argv[1];
    table *data = read_table(filename);
    simulated_annealing(data);
    free_table(data);
    
    return EXIT_SUCCESS;
}
