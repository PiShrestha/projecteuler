#include <stdio.h> // for sprintf
#include <stdbool.h> // for 'bool' , true
#include <string.h>

bool double_palindrome(int num) {
    int base_10 = num;

    char str[20];
    // instead of printing to console, it writes to char array 
    sprintf(str, "%d", base_10);

    int base_2 = num;
    int num_bits = 0;
    while (base_2 > 0) {
        base_2 = base_2 >> 1;
        num_bits += 1;
    }
    
    bool is_base_2_palindrome = false;
    int half = num_bits/2;
    int left_half = num >> half;

    if (num_bits % 2 != 0) {
        left_half = left_half >> 1;
    }
    
    int right_half = (num << (32 - half)) >> (32 - half);

    // reverses the right half of the binary and compares with left
    int reversed = 0;
    for (int i = 0; i < half; i ++) {
        reversed = (reversed << 1) + ((right_half & (1 << i)) >> i);
    }

    if (reversed != left_half) {
        return false;
    }


    for (int i = 0; i < strlen(str)/2; i++) {
        if (str[i] != str[strlen(str) - i - 1]){
            return false;
        }
    }

    return true;
}

int main() {
    int sum = 0;
    for (int i = 0; i < 1000000; i ++) {
        if (double_palindrome(i)) {
            sum += i;
        }
    }
    printf("%d\n", sum);
    printf("%d\n", double_palindrome(7));
}
