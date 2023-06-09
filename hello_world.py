"""
A simple Python script that prints "Hello, World!" to the console.

This script demonstrates the use of functions and the special __name__ variable in Python. It defines a function hello_world that prints "Hello, World!", and a main function that calls hello_world. The main function is only called if the script is being run directly.
"""

def hello_world():
    """
    Prints "Hello, World!" to the console.
    """
    print("Hello, World!")

def main():
    """
    Main function that calls the hello_world function.
    """
    hello_world()

# If this script is being run directly, then call main.
if __name__ == "__main__":
    main()
