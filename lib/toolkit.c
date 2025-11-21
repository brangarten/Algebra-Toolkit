#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//gcc -fPIC -shared -o toolkit.so toolkit.c

/* TODO LIST
* Take in min value and max value
* calculate and store into an array pointer
* access it in python
*/

int domainElements(int least, int greatest) {
    int size = abs(least) + abs(greatest); // incase both vars are negative we can find the number of elements in the domain
    return size;
}
// ax^2 + bx + c
int* calculateQuad(int a, int b, int c, const int minDomain, const int maxDomain) {
    const int SIZE = domainElements(minDomain, maxDomain);
    int* arr = (int*)malloc(SIZE * sizeof(int));
    
    for(int i = minDomain; i <= maxDomain; i++) {
        arr[i] = (a * pow(i, 2)) + (b*i) + c;
    }

    return arr;
}

int* calculateCube(int a, int b, int c, int d, const int minDomain, const int maxDomain) {

}

