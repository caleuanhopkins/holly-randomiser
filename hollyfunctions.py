import json
import random
import os
import shutil

# Inputs running inside function, allows for skipping during tests
def get_user_inputs():
    # Prompt for user input
    windows_user = input("Enter your Windows username: ").strip()
    save_file_name = input("Enter the saved game filename (e.g., Save1): ").strip()

    # Construct the full path to the JSON file
    file_path = fr"C:\Users\{windows_user}\AppData\LocalLow\Weappy\Holly\Saves\Profiles\0\{save_file_name}.json"

    return file_path

# Confirm the file exists and make a backup
def confirm_and_backup(file_path):
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

# Create the randomised data
def update_talent_data(file_path):
    # Load JSON data (handle BOM)
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        obj = json.load(f)

    def recursive_update(o):
        if isinstance(o, dict):
            if o.get("$type") == "Data.GameObject.Character.TalentData, Assembly-CSharp":
                if o.get("id") == 16:
                    return
                if o.get("state") == 0:
                    if isinstance(o.get("professions"), dict):
                        max_value = 0
                        for key in o["professions"]:
                            value = round(random.uniform(0.1, 0.99), 4)
                            o["professions"][key] = value
                            max_value = max(max_value, value)
                        o["limit"] = round(random.uniform(max_value, 1), 4)
                        o["selfEsteem"] = round(random.triangular(-0.9, 0.9, 0.1), 5)
            for key in o:
                recursive_update(o[key])
        elif isinstance(o, list):
            for item in o:
                recursive_update(item)

    recursive_update(obj)
    return obj

# Save the updated data to the file
def save_file_updated_data(data, file_path):
    # Save the updated JSON data
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
