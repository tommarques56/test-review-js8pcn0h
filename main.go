package main

import (
    "fmt"
    "os"
)

// Missing function documentation
func processData(data []int) int {
    sum := 0
    for _, item := range data {
        sum += item
    }
    return sum
}

// Missing error handling
func readFile(filename string) string {
    content, _ := os.ReadFile(filename)  // Error ignored
    return string(content)
}

// Missing input validation
func divide(a, b int) int {
    return a / b  // No division by zero check
}

// Resource not closed properly
func processFile(filename string) {
    file, err := os.Open(filename)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    // File not closed - resource leak
    defer file.Close()
}

// Missing error return
func getValue() int {
    return 42  // Should return (int, error)
}

func main() {
    fmt.Println("Starting Go application...")
    
    data := []int{1, 2, 3, 4, 5}
    result := processData(data)
    fmt.Printf("Result: %d\n", result)
    
    content := readFile("nonexistent.txt")
    fmt.Printf("Content: %s\n", content)
    
    division := divide(10, 0)  // Division by zero
    fmt.Printf("Division: %d\n", division)
    
    processFile("test.txt")
    
    value := getValue()
    fmt.Printf("Value: %d\n", value)
}
