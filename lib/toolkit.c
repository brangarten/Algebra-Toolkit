#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//gcc -fPIC -shared -o toolkit.so toolkit.c

/* TODO LIST
* Take in min value and max value
* calculate and store into an array pointer
* access it in python
*/

int calculateDomainSize(int least, int greatest) {
    int size = abs(least) + abs(greatest); 
    return size;
}

void writeArray(int least, int greatest, int arr[]) {
    for (int i = least; i < greatest; i++) {
        arr[i] = arr[i];
    }
}

// ax^2 + bx + c
void calculateQuad(const int a, const int b, const int c, const int minDomain, const int maxDomain, int array[]) {
        
    const int SIZE = calculateDomainSize(minDomain, maxDomain);
    int xValue = minDomain;
    int yOutput = 0;

    for (int i = 0; i < SIZE; i++) {
        
        int aRes = a * xValue;
        aRes = pow(aRes, 2);

        int bRes = b*xValue;

        int cRes = c;
    
        yOutput = aRes + bRes + c;

        array[i] = yOutput;  

        printf("i: %i x: %d, aRes: %d, bRes: %d, c: %d, output: %d \n", i, xValue, aRes, bRes, cRes, yOutput);
        xValue++;
    }
}

int* calculateCube(int a, int b, int c, int d, const int minDomain, const int maxDomain) {

}

