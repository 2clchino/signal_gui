#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int data(int t){
    srand((unsigned int)time(NULL)+t);
    return rand() % 10 + 1;
}