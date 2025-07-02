import pandas as pd

def check_data_quality(filepath):
    """Loads data from CSV and performs basic quality checks."""
    try:
        df = pd.read_csv(filepath)
        print(f"--- Data Quality Report for {filepath} ---")
        print("\nShape of data (rows, columns):", df.shape)
        print("\nMissing Values per Column:")
        print(df.isnull().sum())
        print("\nDuplicate Rows:", df.duplicated().sum())
        print("\nData Types:")
        print(df.dtypes)
        print("\nBasic Statistics:")
        print(df.describe(include='all'))
        print("------------------------------------------")
        return True 
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    data_file = 'data/sample_data.csv' 
    check_data_quality(data_file)