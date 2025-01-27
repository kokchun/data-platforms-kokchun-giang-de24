from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"

# print(data_path)

with open(data_path / "jokes.json", "r") as file:
    jokes = json.load(file)


pprint(jokes)