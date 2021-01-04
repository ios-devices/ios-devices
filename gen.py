import requests
import json

url = (
    "https://gist.githubusercontent.com/adamawolf/"
    "3048717/raw/Apple_mobile_device_types.txt"
)

if __name__ == "__main__":
    lines = requests.get(url).text.split("\n")

    d = {}
    for line in lines:
        if ":" not in line:
            continue
        name, id = [s.strip() for s in line.split(":")]
        if id in d:
            d[id].append(name)
        else:
            d[id] = [name]

    nd = []
    for k, v in d.items():
        nd.append({
            "name": k,
            "identifiers": v
        })

    jsonStr = json.dumps(nd, indent=4)

    with open("list.json", mode='w') as f:
        f.write(jsonStr)
