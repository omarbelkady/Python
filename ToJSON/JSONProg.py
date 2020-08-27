import json

person = {"name": "Nelan", "age":25, "city":"Austin", "likesC":True, "titles": ["c-lover", "pintos-lover", "assembly-programmer", "programmer", "low-level programmer"]}

JSON5EL2N = json.dumps(person, indent=4, sort_keys=True)
print(JSON5EL2N)

#Dump the json object into a file
with open('nelan.json', 'w') as file:
    json.dump(person, file, indent=5)
