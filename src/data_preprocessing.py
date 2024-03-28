import pandas as pd

def load_dataset(filepath):
    """Load a dataset and return the DataFrame."""
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {filepath}.")
        return df
    except FileNotFoundError:
        print(f"File {filepath} not found. Please check the path.")
        return None
    except Exception as e:
        print(f"An error occurred while loading {filepath}: {e}")
        return None

def verify_dataset(df, expected_rows, expected_cols, dataset_name):
    """Verify the dimensions of a loaded dataset."""
    if df is not None:
        rows, cols = df.shape
        if rows == expected_rows and cols == expected_cols:
            print(f"{dataset_name} dimensions are as expected: {rows} rows, {cols} columns.")
        else:
            print(f"{dataset_name} dimensions unexpected: found {rows} rows and {cols} columns, expected {expected_rows} rows and {expected_cols} columns.")

def main():
    # Expected dimensions
    expected_rows_train = 1600
    expected_cols_train = 19
    expected_rows_test = 400  
    expected_cols_test = 19  

    # Load datasets
    train_df = load_dataset('data/dataset_train.csv')
    test_df = load_dataset('data/dataset_test.csv')

    # Verify datasets
    verify_dataset(train_df, expected_rows_train, expected_cols_train, "Training Dataset")
    verify_dataset(test_df, expected_rows_test, expected_cols_test, "Testing Dataset")

if __name__ == "__main__":
    main()
