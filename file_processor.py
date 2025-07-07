import pandas as pd
import csv

filename = "your_file.csv"

# Open the file
with open(filename, "r", newline='') as f:
    reader = csv.reader(f)
    # Get the header row
    try:
        header = next(reader)
    except Exception as e:
        print("Error reading header:", e)
        exit(1)

    print("Header:", header)
    
    # Loop over the lines, starting with line 2 (first data row)
    for line_num, row in enumerate(reader, start=2):
        try:
            # Try to create a DataFrame with just this row
            _ = pd.DataFrame([row], columns=header)
        except Exception as e:
            print(f"\n❌ Error at line {line_num}:")
            print("Row content:", row)
            print("Error message:", e)
            break  # or continue to find all bad lines

print("\n✅ Done.")
