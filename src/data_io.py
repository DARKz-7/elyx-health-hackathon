import os
import csv
import json
from dataclasses import asdict
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def ensure_data_dir():
    """Ensure that the data directory exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_to_csv(filename, objects, attr_names):
    """
    Save a list of dataclass objects to a CSV file.

    Args:
        filename (str): CSV filename relative to data folder.
        objects (list): List of dataclass instances.
        attr_names (list): List of attribute names for CSV columns.
    """
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=attr_names)
        writer.writeheader()
        for obj in objects:
            row = asdict(obj)
            for key in row:
                # Convert lists and dicts to string for CSV compatibility
                if isinstance(row[key], (list, dict)):
                    row[key] = str(row[key])
                # Convert datetime to ISO format string
                elif isinstance(row[key], datetime):
                    row[key] = row[key].isoformat()
            writer.writerow(row)

def save_to_json(filename, objects):
    """
    Save a list of dataclass objects to a JSON file with datetime handling.

    Args:
        filename (str): JSON filename relative to data folder.
        objects (list): List of dataclass instances.
    """
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)

    def encode(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, '__dataclass_fields__'):
            d = asdict(obj)
            for k, v in d.items():
                if isinstance(v, datetime):
                    d[k] = v.isoformat()
            return d
        return str(obj)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([encode(o) for o in objects], f, indent=2)
