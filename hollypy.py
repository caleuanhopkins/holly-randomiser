import json
import random
import os
import shutil

# Prompt for user input
windows_user = input("Enter your Windows username: ").strip()
save_file_name = input("Enter the saved game filename (e.g., Save1): ").strip()

# Construct the full path to the JSON file
file_path = fr"C:\Users\{windows_user}\AppData\LocalLow\Weappy\Holly\Saves\Profiles\0\{save_file_name}.json"

# Confirm file path with user
print(f"\n📁 Full file path: {file_path}")
confirm = input("Is this correct? (Y/N): ").strip().lower()
if confirm != 'y':
    print("❌ Operation cancelled.")
    exit(0)

# Check if the file exists
if not os.path.exists(file_path):
    print(f"❌ File not found at: {file_path}")
    exit(1)

# Make a backup copy
backup_path = file_path.replace(".json", "_backup.json")
shutil.copyfile(file_path, backup_path)
print(f"📦 Backup created at: {backup_path}")

# Load JSON data (handle BOM)
with open(file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

def update_talent_data(obj):
    """Recursively update target objects in the JSON structure."""
    if isinstance(obj, dict):
        if obj.get("$type") == "Data.GameObject.Character.TalentData, Assembly-CSharp":
            
            # Stops the script from changing Lydia Globe now she's is fixed from 0.8.13EA patch
            if obj.get("id") == 16:
                return

            contract = obj.get("contract", None)

            # Only update if contract is empty or null
            if contract in ("", None):
                # Update 'professions' subproperty values (0.1 to 0.9)
                if isinstance(obj.get("professions"), dict):
                    max_value = 0
                    for key in obj["professions"]:
                        value = round(random.uniform(0.1, 0.99), 4)
                        obj["professions"][key] = value
                        max_value = max(max_value, value)

                    # Set 'limit' to be >= max profession value (up to 1)
                    obj["limit"] = round(random.uniform(max_value, 1), 4)

                    # Set 'selfEsteem' to a value between -0.9 and 0.9, skewed toward -0.3 to 0.4
                    obj["selfEsteem"] = round(random.triangular(-0.9, 0.9, 0.1), 5)

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

print(f"✅ File updated successfully: {file_path}")