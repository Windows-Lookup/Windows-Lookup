# File Tester Tool

## Overview
The **File Tester Tool** is a Python GUI application that allows users to check various properties of a selected file. Built with the `tkinter` library, it displays information such as file size, last modification date, and permissions (readable and writable). This tool is useful for quickly verifying basic information about a file.

## Features
- **File Selection**: Browse and select a file to test.
- **File Properties Display**:
  - Checks if the file exists.
  - Displays the file size in bytes.
  - Shows the last modified date and time.
  - Indicates whether the file is readable and writable.

## Prerequisites
- Python 3.x
- `tkinter` library (comes pre-installed with Python)

## How to Use
1. Run the program by executing the Python script.
2. Click on the **Browse** button to select a file from your system.
3. Click **Test File** to view the file's properties.
4. The file properties will display in the application window.

## Code Overview
- **`test_file` function**: Retrieves and displays file properties, including existence, size, last modified timestamp, and access permissions.
- **`browse_file` function**: Opens a file dialog to allow file selection and updates the file path in the entry field.

## GUI Components
- **File Entry Field**: Displays the selected file path.
- **Browse Button**: Opens the file selection dialog.
- **Test File Button**: Triggers the file test to display properties.
- **Result Display**: Shows the file's properties in a readable format.

## Example Output
Upon selecting a file and clicking **Test File**, the following information might appear:

File Exists: Yes File Size: 2048 bytes Last Modified: 2023-10-12 14:32:45 Readable: Yes Writable: No

csharp
Copy code


## Error Handling
- If no file is selected, an error message prompts the user to select a file.
- If the file does not exist, the program displays an appropriate message.

## License
This project is open-source and available under the MIT License.

## Author
[Your Name]
