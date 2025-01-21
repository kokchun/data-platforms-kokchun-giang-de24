from pathlib import Path
import pandas as pd 

data_path = Path(__file__).parent / "data"

print(data_path / "prog_book.csv")

df = pd.read_csv(data_path / "prog_book.csv")
print(df.head())