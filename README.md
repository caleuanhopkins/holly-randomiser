# Hollywood Animal - Free Agents Randomiser

This Python script updates specific properties in a JSON file containing game character talent data. It is designed to target objects with a specific `$type`, and only modifies them if their `"contract"` field is empty.


## 🔧 What It Does

For each object where:
- `$type` is `"Data.GameObject.Character.TalentData, Assembly-CSharp"`, **and**
- `"contract"` is either empty (`""`) or missing

It will:
- Randomly update each value in the `"professions"` dictionary to a float between `0` and `1`.
- Set `"limit"` to a float between the maximum value in `"professions"` and `1`.
- Set `"selfEsteem"` based on the highest `"professions"` value:
  - If max value > `0.5`: `"selfEsteem"` is between `0.5` and `1`
  - If max value ≤ `0.5`: `"selfEsteem"` is between `0.0001` and `0.49999`


## 📌 Notes
* Be sure to back up your original JSON file before running the script if you need to retain the original data.
* You can run this script against any save file from the very start of the game.
* **HOWEVER:** This may also impact the quality of staff at other movie studios as the game appears to make all staff "free agents" when the file is created by the game, and then assigns them at random as the game progresses (This is being investigated to confirm this theory). 
* **RECOMMENDED:** I recommend you wait until you have casting office and the ability to hire all staff types before running this script.


## 📁 Input

A JSON file named `savedGame.json` should be present in the same directory as the script. It is recommended that you run this script outside of your saved games directory and make a copy of your saved game file before running this script.

## 💾 Output

The script overwrites the original `savedGame.json` with updated content. The structure is preserved, and only qualifying objects are modified. Once modified, copy the `savedGame.json` back into your saved games directory, rename it back to your original studio name, and then reload the saved file.


## ✅ Requirements

- Python 3.x  
No external dependencies are required.


## 🪟 Installing Python on Windows (via Microsoft Store)

The simplest way to install Python on Windows is through the Microsoft Store:

1. Open the **Microsoft Store** from your Start menu.
2. Search for **"Python"**.
3. Choose the latest version of **Python 3.x** published by the **Python Software Foundation**.
4. Click **Get** or **Install**.
5. Once installed, open Command Prompt and verify the installation:
   ```bash
   python --version
6. You should see something like Python 3.11.x.
   `✅ Python installed via the Microsoft Store is automatically added to your system PATH.`


## 🚀 How to Run the Script

1. Download or copy the script into a file named hollypy.py.
2. Copy your save game file that you want to edit, copy it to the same directory as the `hollypy.py` file, rename the `.json` file to `savedGame.json`.
3. Open Command Prompt in that folder:
    * Press Shift + Right Click in the folder background
    * Choose "Open PowerShell window here" or "Open Command Window here"
4. Run the script: `python hollypy.py`
5. Once complete, your savedGame.json file will be updated with the changes.
6. Copy the updated `savedGame.json` file to your saved games directory and rename it back to your original save game file. **NOTE:** Ensure you keep a copy of your original save game, don't overwrite this the original save game with this update version unless you have a backup of the original save game file stored somewhere.
7. in Hollywood Animal game, load the updated saved game