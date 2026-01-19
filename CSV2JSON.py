import pandas as pd

# Load the CSV
df = pd.read_csv('Mol_Sluis_Dessel_data.csv')

# Convert to JSON (orient='records' creates an array of objects)
df.to_json('output.json', orient='records', indent=4)