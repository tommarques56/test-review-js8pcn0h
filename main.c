#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Missing function documentation
int calculate_sum(int a, int b) {
    return a + b;
}

// Memory leak - allocated memory not freed
char* create_string() {
    char* str = malloc(100);
    strcpy(str, "Hello World");
    return str;  // Memory leak
}

// Buffer overflow vulnerability
void copy_string(char* dest, char* src) {
    strcpy(dest, src);  // No bounds checking
}

// Uninitialized variable
int get_value() {
    int value;  // Uninitialized
    return value;
}

int main() {
    printf("Starting C application...\n");
    
    char* str = create_string();
    printf("String: %s\n", str);
    // Memory leak - str not freed
    
    char buffer[10];
    char input[] = "This is a very long string that will overflow";
    copy_string(buffer, input);  // Buffer overflow
    
    int val = get_value();
    printf("Value: %d\n", val);  // Undefined behavior
    
    return 0;
}
