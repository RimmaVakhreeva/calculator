Running the Build Script for Calculator App

Follow these instructions to run the build script, which will execute unit tests and create a distributable package for the application.

Prerequisites:
- Python 3.x installed
- Access to a terminal or command-line interface

Instructions:

1. Open your terminal or command prompt.

2. Navigate to the project directory:
   Change the directory to where your project is located using the cd command.
   cd path/to/calculator_app

3. Make sure the build script is executable:
   If you haven't already, change the permissions of the build script to make it executable.
   chmod +x build_and_test.sh

4. Run the build script:
   Execute the build script by typing the following command:
   ./build_and_test.sh

The script will first run all unit tests. If the tests pass, it will then create a source distribution and a wheel for the project, which you can find in the dist/ directory.

If you encounter any issues, make sure you have Python installed and your current working directory is the root of the project.
