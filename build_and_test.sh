#!/bin/bash

# Step 1: Run unit tests
echo "Running unit tests..."
python -m unittest discover -s . -p "test_*.py"

# Check if tests were successful
if [ $? -ne 0 ]; then
    echo "Unit tests failed."
    exit 1
fi

# Step 2: Create a distributable package
echo "Creating a distributable package..."
python setup.py sdist bdist_wheel

echo "Build and test script completed successfully."
