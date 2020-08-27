#json file to dictionary
import json

indiv = {"name": "Nelan", "age":25, "city":"Austin", "likesC":True, "titles": ["c-lover", "pintos-lover", "assembly-programmer", "programmer", "low-level programmer"]}

JSON6EL2N = json.dumps(indiv, indent=4, sort_keys=True)
#print(JSON6EL2N)

indiv= json.loads(JSON6EL2N)
print(indiv)
