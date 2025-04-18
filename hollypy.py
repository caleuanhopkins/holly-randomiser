import json
import random

# Path to your JSON file
file_path = 'savedGame.json'

# Load JSON data (handle BOM)
with open(file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

def update_talent_data(obj):
    """Recursively update target objects in the JSON structure."""
    if isinstance(obj, dict):
        if obj.get("$type") == "Data.GameObject.Character.TalentData, Assembly-CSharp":
            contract = obj.get("contract", None)

            # Only update if contract is empty or null
            if contract in ("", None):
                # Update 'professions' subproperty values (0 to 1)
                if isinstance(obj.get("professions"), dict):
                    max_value = 0
                    for key in obj["professions"]:
                        value = round(random.uniform(0, 1), 4)
                        obj["professions"][key] = value
                        max_value = max(max_value, value)

                    # Set 'limit' to be >= max profession value (up to 1)
                    obj["limit"] = round(random.uniform(max_value, 1), 4)

                    # Set selfEsteem based on threshold of max profession value
                    if max_value > 0.5:
                        obj["selfEsteem"] = round(random.uniform(0.5, 1), 5)
                    else:
                        obj["selfEsteem"] = round(random.uniform(0.0001, 0.49999), 5)

        else:
            for key in obj:
                update_talent_data(obj[key])
    elif isinstance(obj, list):
        for item in obj:
            update_talent_data(item)

# Apply the update
update_talent_data(data)

# Save the updated JSON data
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
