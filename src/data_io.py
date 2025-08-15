import csv
import json
import os
from dataclasses import asdict
from datetime import datetime

def save_to_csv(filename, objects, attr_names):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=attr_names)
        writer.writeheader()
        for obj in objects:
            row = asdict(obj)
            for key in row:
                if isinstance(row[key], (list, dict)):
                    row[key] = str(row[key])
            writer.writerow(row)

def save_to_json(filename, objects):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        def encode(obj):
            if isinstance(obj, (datetime)):
                return obj.isoformat()
            if hasattr(obj, '__dataclass_fields__'):
                d = asdict(obj)
                for k, v in d.items():
                    if isinstance(v, (datetime)):
                        d[k] = v.isoformat()
                return d
            return str(obj)
        json.dump([encode(o) for o in objects], f, indent=2)
