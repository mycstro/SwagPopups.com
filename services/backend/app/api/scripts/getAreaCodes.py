import pandas as pd
import json
from flask import requests

def download_nanpa_file(url, output_filename):
    headers = {
        # Mimic a common browser user-agent
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    }
    
    try:
        print("Attempting to download the file...")
        response = requests.get(url, headers=headers, allow_redirects=True, timeout=30)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        
        # Write content to file in binary mode
        with open(output_filename, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully and saved as '{output_filename}'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.status_code}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

# Load the Excel file (adjust the sheet name if needed)
df = pd.read_excel("NANPA_area_codes.xlsx", sheet_name=0)

# Inspect the columns to find the area code column (change "Area Code" as needed)
print(df.columns)

# Extract and clean the area codes column
area_codes = df["Area Code"].dropna().unique().tolist()

# Optionally, sort the area codes
area_codes.sort()

# Save the clean list to a JSON file for easy consumption later
with open("area_codes.json", "w") as f:
    json.dump(area_codes, f, indent=2)

print("Extracted area codes:", area_codes)

# Additional steps for further processing or analysis, e.g., creating a dictionary for faster lookup

area_code_dict = {code: df[df["Area Code"] == code].iloc[0]["Area Name"].strip() for code in area_codes}
print("Area code dictionary:", area_code_dict)

# Example usage of the area code dictionary:

print(area_code_dict.get("555"))  # Output: "Pittsburgh"
print(area_code_dict.get("123"))  # Output: None (not found)

# You can now use this JSON file for faster lookups in your application or API.

# To convert the JSON file back to a Pandas DataFrame for further processing:

df_area_codes = pd.read_json("area_codes.json")
print(df_area_codes)

# Note: The JSON file is created in the same directory as the script, so make sure to adjust the file path if necessary.


if __name__ == "__main__":
    url = "https://example.com/path/to/NANPA_area_codes.xlsx"
    output_filename = "NANPA_area_codes.xlsx"
    download_nanpa_file(url, output_filename)
    # Continue with the remaining steps as described above.
    # You can now use the "area_codes.json" file for further processing or analysis.
    # Make sure to replace "https://example.com/path/to/NANPA_area_codes.xlsx" with the actual URL of the NANPA area code Excel file.
    # Also, adjust the "output_filename" and "Area Code" column names as needed.
    # After processing, you can save the clean list to a JSON file for easy consumption later.
    