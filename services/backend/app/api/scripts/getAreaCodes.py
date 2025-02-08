import pandas as pd
import json
import requests
import io

import pandas as pd

pd.set_option('display.max_rows', 500)  # or use None to display all rows

def clean_and_filter_nanpa_df(raw_data: bytes) -> pd.DataFrame:
    """
    Cleans up NANPA CSV data (provided as raw bytes) by:
      1. Skipping the first row (e.g., file metadata/header) and reading the CSV data.
      2. Keeping only the columns: NPA_ID, LOCATION, COUNTRY, and IN_SERVICE.
      3. Removing any rows where IN_SERVICE is 'N' (case-insensitive).
      4. Dropping the last column (IN_SERVICE) while preserving NPA_ID (if it is the first column).
      5. Joining the LOCATION and COUNTRY columns (with a space) into a new column LOCATION_COUNTRY.
    
    Parameters:
        raw_data (bytes): The raw CSV data as bytes.

    Returns:
        pd.DataFrame: A DataFrame with NPA_ID (if present) and LOCATION_COUNTRY.
    """
    # Convert raw bytes to a string wrapped in a StringIO object.
    dfg = io.StringIO(raw_data.decode('utf-8'))
    dfg.seek(0)  # Ensure the pointer is at the start.

    try:
        # Read the CSV data, skipping the first row which contains metadata.
        df = pd.read_csv(dfg, skiprows=1)
    except Exception as e:
        raise RuntimeError(f"Error reading CSV data: {e}")

    # Define the columns we want to keep.
    columns_to_keep = ["NPA_ID", "LOCATION", "COUNTRY", "IN_SERVICE"]

    # Ensure all desired columns are present.
    missing_cols = set(columns_to_keep) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing expected columns in DataFrame: {missing_cols}")

    # Keep only the specified columns.
    df_clean = df[columns_to_keep].copy()

    # Remove rows where IN_SERVICE equals "N" (ignoring extra whitespace and case).
    df_clean = df_clean[df_clean["IN_SERVICE"].astype(str).str.strip().str.upper() != "N"]

    # Drop only the last column ("IN_SERVICE"); do not remove NPA_ID.
    df_temp = df_clean.drop(columns=["IN_SERVICE"]).copy()

    # Join the LOCATION and COUNTRY columns with a space to form a new column.
    # We assume these are the last two columns in df_temp.
    df_temp["LOCATION_COUNTRY"] = df_temp["LOCATION"].astype(str) + " " + df_temp["COUNTRY"].astype(str)

    # Final output: if NPA_ID exists, include it; otherwise, just the joined column.
    if "NPA_ID" in df_temp.columns:
        df_final = df_temp[["NPA_ID", "LOCATION_COUNTRY"]].copy()
    else:
        df_final = df_temp[["LOCATION_COUNTRY"]].copy()

    return df_final

# -------------------------------
# Example Usage:
# -------------------------------
if __name__ == "__main__":
    import requests

    url = "https://reports.nanpa.com/public/npa_report.csv"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        try:
            cleaned_df = clean_and_filter_nanpa_df(response.content)
            print("Final Cleaned DataFrame:")
            print(cleaned_df.head())
            print( cleaned_df)
        except Exception as e:
            print("Error cleaning data:", e)
    else:
        print(f"Failed to download data. HTTP status code: {response.status_code}")

