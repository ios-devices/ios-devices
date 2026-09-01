"""Generate list.json from Apple's device identifier gist."""

import json
from collections import defaultdict
from pathlib import Path
from typing import TypedDict

import requests

url = "https://gist.githubusercontent.com/adamawolf/3048717/raw/Apple_mobile_device_types.txt"


class DeviceEntry(TypedDict):
    """A single entry in list.json."""

    name: str
    identifiers: list[str]


if __name__ == "__main__":
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    lines = response.text.splitlines()

    d: defaultdict[str, list[str]] = defaultdict(list)
    for line in lines:
        if ":" not in line:
            continue
        identifier, name = [s.strip() for s in line.split(":", maxsplit=1)]
        d[name].append(identifier)

    nd: list[DeviceEntry] = [{"name": k, "identifiers": v} for k, v in d.items()]

    Path("list.json").write_text(json.dumps(nd, indent=4))
