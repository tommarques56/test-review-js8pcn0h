#!/usr/bin/env python3
"""
Sample Python file with various code issues for testing.
"""

import os
import sys

def process_data(data):
    """Process some data."""
    print(f"Processing data: {data}")  # Should use logging
    result = data * 2
    print(f"Result: {result}")  # Should use logging
    return result

def calculate_sum(a, b):
    return a + b  # Missing docstring

def dangerous_eval(user_input):
    """Dangerous function using eval."""
    return eval(user_input)  # Security risk

def main():
    print("Starting application...")  # Should use logging
    
    # Simulate some processing
    data = [1, 2, 3, 4, 5]
    for item in data:
        print(f"Processing item: {item}")  # Should use logging
        result = process_data(item)
        print(f"Item {item} processed: {result}")  # Should use logging
    
    print("Application completed!")  # Should use logging

if __name__ == "__main__":
    main()
