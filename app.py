#!/usr/bin/env python3
"""
Simple test application for Jenkins CI/CD pipeline
"""

def add(a, b):
    """Simple add function to test"""
    return a + b

def multiply(a, b):
    """Simple multiply function to test"""
    return a * b

def main():
    print("=" * 40)
    print("Jenkins Test Application")
    print("=" * 40)
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print("Application ran successfully!")
    print("=" * 40)

if __name__ == "__main__":
    main()
