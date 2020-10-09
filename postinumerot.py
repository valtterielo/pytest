import json
from pathlib import Path

source = Path("node_modules/datasets-fi-postalcodes/")
data = source / "postcode_map_light.json"
f = open(data)
postinumerolista = json.loads(f.read())

results = []

def etsi_postinumerot(postitoimipaikka, postinumerot_sanakirja):
    
    for postinumero, kaupunki in postinumerot_sanakirja.items():
        if postitoimipaikka.upper() == kaupunki:
            results.append(postinumero)
 
    for i in results:
        print(i)
    
    

