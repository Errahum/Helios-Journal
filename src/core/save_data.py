import os
import json


def save_entry(date, text):
    entry = {"date": date, "text": text.strip()}
    if not os.path.exists("entries"):
        os.makedirs("entries")
    file_path = os.path.join("entries", "entries.jsonl")

    entries = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                existing_entry = json.loads(line)
                # Si entrée avec même date existe déjà, la remplacer
                if existing_entry["date"] == date:
                    continue
                entries.append(existing_entry)

    # Ajouter ou remplacer entrée
    entries.append(entry)

    with open(file_path, "w", encoding="utf-8") as file:
        for entry in entries:
            file.write(json.dumps(entry) + "\n")
