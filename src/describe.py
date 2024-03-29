import os
import pandas as pd
import sys
import numpy as np
from tabulate import tabulate

def calculate_mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def calculate_std_dev(numbers):
    if len(numbers) == 0:
        return None
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

def calculate_min(numbers):
    return min(numbers)

def calculate_max(numbers):
    return max(numbers)

def calculate_percentile(numbers, percentile):
    numbers.sort()
    index = (len(numbers) - 1) * percentile
    lower = numbers[int(index)]
    upper = numbers[min(int(index) + 1, len(numbers) - 1)]
    return lower + (upper - lower) * (index % 1)


def describe_dataset(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        raise ValueError(f"No file found at: {filepath}")
    descriptions = {}
    for column in df:
        if df[column].dtype in [np.int64, np.float64]:  # Only calculate for numerical columns
            numbers = df[column].dropna().tolist()  # Exclude NaN values
            if numbers:  # Only calculate descriptions if numbers is not empty
                descriptions[column] = {
                    'Count': len(numbers),
                    'Mean': calculate_mean(numbers),
                    'Std': calculate_std_dev(numbers),
                    'Min': calculate_min(numbers),
                    '25%': calculate_percentile(numbers, 0.25),
                    '50%': calculate_percentile(numbers, 0.50),
                    '75%': calculate_percentile(numbers, 0.75),
                    'Max': calculate_max(numbers),
                }
    return descriptions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Please provide a filepath as an argument")
    filepath = sys.argv[1]
    descriptions = describe_dataset(filepath)
    headers = [""] + list(descriptions.keys())

    table = []
    for stat in ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']:
        row = [stat] + [descriptions[column].get(stat, '') for column in descriptions.keys()]
        table.append(row)
    print(tabulate(table, headers, tablefmt="pipe"))  # print as a markdown table