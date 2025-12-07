#!/usr/bin/python3
import imp
import sys

def discover_hidden_names():
    # Load the hidden_4.pyc file from /tmp
    try:
        hidden_module = imp.load_compiled("hidden_4", "/tmp/hidden_4.pyc")
    except FileNotFoundError:
        print("The file hidden_4.pyc was not found in /tmp.")
        sys.exit(1)
    
    # Get the names defined in the module, excluding those that start with '__'
    names = dir(hidden_module)
    filtered_names = [name for name in names if not name.startswith("__")]
    
    # Sort the names alphabetically
    filtered_names.sort()

    # Print each name on a new line
    for name in filtered_names:
        print(name)

# This ensures the code does not run when the script is imported as a module
if __name__ == "__main__":
    discover_hidden_names()

