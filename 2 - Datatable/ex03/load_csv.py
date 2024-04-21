import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Loads a CSV file into a pandas DataFrame and prints its shape."""
    try:
        dataset = pd.read_csv(path)
        print("Loading dataset of dimensions", dataset.shape)
        return dataset
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
