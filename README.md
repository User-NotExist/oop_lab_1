# Lab overview
Processing data from csv file using OOP principle. Dataset contains sample city and temperature. 

# Program structure
- data_processing.py
    + Main python script containing all logic to process the data.
- README.md
    + The thing that you are currently reading, duh
- Cities.csv
    + Sample dataset.

# Design Overview

### DataLoader Class

The `DataLoader` class handles file operations and CSV data loading.

**Attributes:**
- `base_path`: Path object representing the directory where data files are located

**Key Methods:**
- `__init__(base_path=None)`: Initializes the DataLoader with an optional base path
- `load_csv(filename)`: Loads a CSV file and returns its contents as a list of dictionaries

### Table Class

The `Table` class represents a tabular dataset and provides methods for data manipulation and analysis.

**Attributes:**
- `table`: List of dictionaries containing the actual data

**Key Methods:**
- `__init__(table)`: Initializes a Table with data
- `filter(condition)`: Filters the table based on a lambda function condition and returns a new Table
- `aggregate(aggregation_function, aggregation_key)`: Performs aggregation operations on specified columns

# Running Instructions
1. Ensure you have Python installed on your machine.
2. Place the `data_processing.py` and `Cities.csv` files in the same directory
3. Run the following command in your terminal:
   ```bash
   python3 data_processing.py
   ```
