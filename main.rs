// Sample Rust file with various issues
use std::collections::HashMap;

// Missing documentation
fn process_data(data: &[i32]) -> i32 {
    let mut sum = 0;
    for item in data {
        sum += item;
    }
    sum
}

// Unnecessary unwrap() usage
fn get_value() -> i32 {
    let result: Result<i32, &str> = Ok(42);
    result.unwrap()  // Should use proper error handling
}

// Missing error handling
fn divide(a: i32, b: i32) -> i32 {
    a / b  // No division by zero check
}

// Using unsafe code unnecessarily
unsafe fn unsafe_operation(ptr: *mut i32) {
    *ptr = 42;  // Unsafe operation
}

// Missing lifetime parameters
fn get_string() -> &str {
    "Hello"  // Lifetime issue
}

fn main() {
    println!("Starting Rust application...");
    
    let data = vec![1, 2, 3, 4, 5];
    let result = process_data(&data);
    println!("Result: {}", result);
    
    let value = get_value();
    println!("Value: {}", value);
    
    let division = divide(10, 0);  // Division by zero
    println!("Division: {}", division);
    
    let mut x = 42;
    unsafe {
        unsafe_operation(&mut x);
    }
    println!("Unsafe result: {}", x);
}
