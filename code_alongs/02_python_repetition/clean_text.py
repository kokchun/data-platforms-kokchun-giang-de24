import re 
from pathlib import Path

print("This is path of this script")

data_path = Path(__file__).parent / "data"

with open(data_path / "ml_text_raw.txt", 'r') as file:
    raw_text = file.read()


text_fixed_spacing = re.sub(r"\s+", " ",raw_text)

# similar code as in jupyter notebook for cleaning the rest of the text

print(text_fixed_spacing)