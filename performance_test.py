#!/usr/bin/env python3
"""
File with performance improvements for testing.
"""

import time
from functools import lru_cache

def efficient_sort(data):
    """Efficient built-in sort."""
    return sorted(data)

@lru_cache(maxsize=128)
def fast_fibonacci(n):
    """Fast fibonacci with memoization."""
    if n <= 1:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)

def process_large_list_efficient(data):
    """Process large list efficiently using list comprehension."""
    return [data[i] * data[j] for i in range(len(data)) for j in range(len(data))]

def main():
    print("Testing performance improvements...")
    
    # Test efficient sort
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = efficient_sort(data.copy())
    print(f"Sorted: {sorted_data}")
    
    # Test fast fibonacci
    print(f"Fibonacci(10): {fast_fibonacci(10)}")
    
    # Test efficient large list processing
    large_data = list(range(100))
    processed = process_large_list_efficient(large_data)
    print(f"Processed {len(processed)} items")

if __name__ == "__main__":
    main()
