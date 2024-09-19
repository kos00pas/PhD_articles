#include <stdio.h>

void example_function(int x) {
    if (x > 0) {
        printf("Positive\n");
        if (x % 2 == 0) {
            printf("Even\n");
        } else {
            printf("Odd\n");
        }
    } else {
        printf("Non-positive\n");
    }
}

int main() {
    int x;
    scanf("%d", &x);  // Input for symbolic execution
    example_function(x);
    return 0;
}
