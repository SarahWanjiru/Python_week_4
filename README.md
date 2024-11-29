# Python_week_4
Week 4: File Handling and Exception Handling

# File Read & Write Challenge 🖋️ & Error Handling Lab 🧪

## Overview
This project provides two Python programs:

1. **File Read & Write Challenge**: Reads the content of a file, modifies it, and writes the result to a new file.
2. **Error Handling Lab**: Handles file-related errors gracefully when attempting to read a file based on user input.

## How to Use

### File Read & Write Challenge

This program reads content from an input file, transforms the text (e.g., converting it to uppercase), and writes the modified content to an output file.

**Example Usage**:
```python
# Provide input and output filenames
input_file = "example.txt"
output_file = "modified_example.txt"

# Run the function to modify and write the file content
read_and_write(input_file, output_file)
```

**Output**:
- If `example.txt` exists, its content is converted to uppercase and saved in `modified_example.txt`.
- If an error occurs (e.g., the file doesn't exist), the program handles it and displays an appropriate error message.

### Error Handling Lab

This program asks the user for a filename, attempts to read it, and handles errors like non-existent files or permission issues.

**Example Usage**:
```python
# Run the function to handle file reading with error handling
error_handling_lab()
```

**Output**:
- If the file exists, its content is displayed.
- If the file does not exist, an error message is shown: `Error: The file 'filename' does not exist.`
- If permission is denied, an appropriate error is shown: `Error: Permission denied for file 'filename'.`

## Code Explanation

### File Read & Write Challenge
- The program uses the `with` statement to handle file opening and closing automatically.
- The `try-except` block handles potential errors like `FileNotFoundError` and `IOError`.

### Error Handling Lab
- Uses `input()` to prompt the user for a filename.
- Handles `FileNotFoundError`, `PermissionError`, and `IOError` for a robust user experience.

## Learning Resources

- **Python Documentation**: [File I/O in Python](https://docs.python.org/3/tutorial/inputoutput.html)
- **W3Schools Python File Handling**: [File Handling Tutorial](https://www.w3schools.com/python/python_file_handling.asp)
- **Python Error Handling**: [Exception Handling in Python](https://realpython.com/python-exceptions/)
- **Automate the Boring Stuff with Python** by Al Sweigart: [Book for Python Automation](https://automatetheboringstuff.com/)
- **Python Programming on Codecademy**: [Interactive Course](https://www.codecademy.com/learn/learn-python-3)

Feel free clone the repository and start working on this project. You can to modify the code to fit your learning goals or extend it with additional error handling and functionalities!
