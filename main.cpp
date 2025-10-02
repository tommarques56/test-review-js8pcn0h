#include <iostream>
#include <vector>
#include <memory>

using namespace std;

// Missing class documentation
class DataProcessor {
private:
    int* data;
    size_t size;
    
public:
    // Raw pointer instead of smart pointer
    DataProcessor(int* d, size_t s) : data(d), size(s) {}
    
    // Missing destructor - memory leak
    ~DataProcessor() {
        // Should delete[] data;
    }
    
    // Missing const correctness
    int process() {
        int sum = 0;
        for (size_t i = 0; i < size; i++) {
            sum += data[i];
        }
        return sum;
    }
};

// Using raw arrays instead of std::vector
void process_array(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << "Processing: " << arr[i] << endl;  // Should use logging
    }
}

// Exception safety issues
int divide(int a, int b) {
    return a / b;  // No division by zero check
}

int main() {
    cout << "Starting C++ application..." << endl;
    
    int* raw_array = new int[5]{1, 2, 3, 4, 5};  // Raw pointer
    DataProcessor processor(raw_array, 5);
    
    int result = processor.process();
    cout << "Result: " << result << endl;
    
    // Memory leak - raw_array not deleted
    
    int division = divide(10, 0);  // Division by zero
    cout << "Division: " << division << endl;
    
    return 0;
}
