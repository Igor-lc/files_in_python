import json

with open("example.json") as f:
    j_data = f.read()
    data = json.loads(j_data)
    print(data)

print()

with open("example.json") as f:
    d = json.load(f)
    print(d)
