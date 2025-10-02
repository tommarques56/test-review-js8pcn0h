#!/usr/bin/env python3
"""
File with security improvements for testing.
"""

import os
import subprocess
import ast
import re

def execute_command_safe(user_input):
    """Execute command safely with input validation."""
    # Validate input to prevent injection
    if not re.match(r'^[a-zA-Z0-9\s\-_]+$', user_input):
        raise ValueError("Invalid input: only alphanumeric characters allowed")
    
    # Use subprocess instead of os.system
    result = subprocess.run(['echo', user_input], capture_output=True, text=True)
    return result.stdout

def evaluate_expression_safe(expr):
    """Evaluate mathematical expression safely."""
    # Use ast.literal_eval instead of eval
    try:
        result = ast.literal_eval(expr)
        return result
    except (ValueError, SyntaxError):
        raise ValueError("Invalid expression")

def read_file_safe(filename):
    """Read file with validation."""
    # Validate filename
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File {filename} not found")
    
    if not filename.endswith(('.txt', '.py', '.json')):
        raise ValueError("Invalid file type")
    
    with open(filename, 'r') as f:
        return f.read()

def main():
    try:
        user_input = input("Enter command: ")
        result = execute_command_safe(user_input)
        print(f"Result: {result}")
        
        expr = input("Enter expression: ")
        result = evaluate_expression_safe(expr)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
