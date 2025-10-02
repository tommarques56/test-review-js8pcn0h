#!/usr/bin/env python3
"""
Sample Python file with various code issues for testing.
"""

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_data(data):
    """Process some data."""
    logger.info(f"Processing data: {data}")
    result = data * 2
    logger.info(f"Result: {result}")
    return result

def calculate_sum(a, b):
    """Calculate sum of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Sum of a and b
    """
    return a + b

def main():
    logger.info("Starting application...")
    
    # Simulate some processing
    data = [1, 2, 3, 4, 5]
    for item in data:
        logger.info(f"Processing item: {item}")
        result = process_data(item)
        logger.info(f"Item {item} processed: {result}")
    
    logger.info("Application completed!")

if __name__ == "__main__":
    main()
