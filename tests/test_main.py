import sys
import os
import pandas as pd

# Add the src directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import load_and_process_data

def test_no_duplicates():
    """Test if duplicate rows are removed."""
    # Load the data and process it
    df = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")

    # Load the processed dataset
    processed_df = pd.read_csv("data/test_processed_dataset.csv")

    # Assert there are no duplicates in the processed DataFrame
    assert processed_df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
