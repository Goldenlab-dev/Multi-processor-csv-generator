
# Multi-Processor CSV Generator

A multi-processor ultra-fast and optimized CSV combination generator with file integrity check.

## Overview

This project is a Python script designed to generate all possible combinations of a specified length using a given set of characters. The script leverages multi-processing to speed up the generation process and ensures file integrity by verifying the final output.

## Features

- Generates combinations of characters including lowercase, uppercase, numbers, and special characters.
- Supports multi-processing to optimize the generation process.
- Concatenates partial results into a final CSV file.
- Verifies the integrity of the final CSV file to ensure all combinations are generated correctly.

## How to Use

### Prerequisites

- Python 3.x
- Multiprocessing support on your operating system

### Script Execution

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the command:
   ```bash
   python main.py
   ```

### User Input Prompts

Upon running the script, you will be prompted to provide the following inputs:

1. **Include lowercase characters (a-z)? (y/n):**
   - Enter 'y' to include lowercase characters.
   - Enter 'n' to exclude lowercase characters.

2. **Include uppercase characters (A-Z)? (y/n):**
   - Enter 'y' to include uppercase characters.
   - Enter 'n' to exclude uppercase characters.

3. **Include numbers (0-9)? (y/n):**
   - Enter 'y' to include numbers.
   - Enter 'n' to exclude numbers.

4. **Include special characters? (y/n):**
   - Enter 'y' to include special characters.
   - Enter 'n' to exclude special characters.

5. **Enter the desired length of combinations:**
   - Enter the length of the combinations you want to generate (e.g., 3 for all possible combinations of length 3).

6. **Enter the custom path for the CSV (leave blank for project root):**
   - Enter a path where you want the final CSV file to be saved. Leave blank to save in the current directory.

7. **Enter the final filename for the CSV (without .csv extension):**
   - Provide a name for the final CSV file.

8. **How many processes do you want to use? (1-n):**
   - Enter the number of processes to use for generation. It is recommended to use a number up to the maximum number of CPU cores available.

### Example

```bash
Include lowercase characters (a-z)? (y/n): y
Include uppercase characters (A-Z)? (y/n): y
Include numbers (0-9)? (y/n): y
Include special characters? (y/n): n
Enter the desired length of combinations: 3
Enter the custom path for the CSV (leave blank for project root): 
Enter the final filename for the CSV (without .csv extension): combinations
How many processes do you want to use? (1-8): 4
```

### Output

The script will generate a CSV file with all possible combinations of the specified length using the selected character sets. The CSV file will be saved in the specified directory with the provided filename.

### File Integrity Check

After generating the CSV file, the script will verify the integrity of the file by checking the total number of combinations and the length of each combination. If any discrepancies are found, an error message will be displayed.

## Script Details

### Functions

- **`create_dataset(lower, upper, numbers, special)`**: Creates the dataset of characters based on user inputs.
- **`combination_worker(task)`**: Generates combinations and writes them to a partial CSV file.
- **`concatenate_parts(filename, num_parts, lock)`**: Concatenates partial CSV files into the final CSV file.
- **`main()`**: Main function to handle user inputs, distribute tasks, and verify the final output.

### Multi-Processing

The script uses the `multiprocessing` module to divide the task into multiple processes, each generating a portion of the total combinations. The partial results are then concatenated into a single CSV file.

### File Integrity Verification

After generating the final CSV file, the script reads the file to ensure that all combinations are present and that each combination has the correct length.

## Conclusion

This project provides an efficient and scalable way to generate large sets of combinations using multi-processing in Python. The script ensures that all combinations are generated correctly and verifies the integrity of the final output, making it a reliable tool for generating combination datasets.

Feel free to report any issues.
