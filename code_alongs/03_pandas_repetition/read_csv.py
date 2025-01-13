import pandas as pd 
from pathlib import Path

# print(Path(__file__).parent / "data")

data_path = Path(__file__).parent / "data"

df = pd.read_csv(data_path / "calories.csv")

print(df.head())