#include <stdio.h>

char* display(char* str, int age) {
    printf("im %s and i'm %d\n", str, age);
    return "maou";
}

int add(int x, int y) {
    return x+y;
}

int sumArr(int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}