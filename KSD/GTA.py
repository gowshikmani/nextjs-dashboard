import pandas as pd

# Import CSV as DataFrame
de = pd.read_csv("GTA.csv")

# Display as a table
print(de.to_string(index=False))
