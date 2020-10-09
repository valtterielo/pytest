import json
from pathlib import Path

source = Path("node_modules/datasets-fi-postalcodes/")
data = source / "postcode_map_light.json"
f = open(data)

postinumerot = json.loads(f.read())
postinro = input("Kirjoita postinumero: ")

print(postinumerot[postinro])
