"""Shared project helpers."""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_json(relative_path):
    with (BASE_DIR / relative_path).open("r", encoding="utf-8") as file:
        return json.load(file)

def money(value):
    return f"Rs. {value:,.2f}"
