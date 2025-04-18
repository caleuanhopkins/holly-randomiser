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

## ✅ Requirements

- Python 3.x  
No external dependencies are required.


## 🚀 How to Run the Script

1. Download latest [release package](https://github.com/caleuanhopkins/holly-randomiser/releases) and extract the `holly-randomiser` directory somewhere
2. Inside the extract directorty, run the script: `python hollypy.py`
3. When you run the script, you’ll be prompted to enter:
   * Your **Windows username** (e.g., `john` if your path is `C:\Users\john`)
   * The **save file name** (e.g., `Save1`)
   * Together, these will set the save game file path to: `C:\Users\john\AppData\LocalLow\Weappy\Holly\Saves\Profiles\0\Save1.json`
   ```bash
      Enter your Windows username: john
      Enter the saved game filename (e.g., Save1): Save1
      📁 Full file path: C:\Users\john\AppData\LocalLow\Weappy\Holly\Saves\Profiles\0\Save1.json
      Is this correct? (Y/N):
4. After entering your username and save file name, you'll see the full path displayed. You'll be asked to confirm it's correct before any changes are made.
   * When confirmed, a copy of your original saved game will be created and saved in the same directory with `_backup` appended to the file name, should you need to recover the original saved game file
5. Once done, the script will update the saved game file and override the save game file (remember a `_backup` version of your saved is in the directory for recovery purposes)
6. In Hollywood Animal game, load the updated saved game

## 📌 Notes
* You can run this script against any save file from the very start of the game.
* **HOWEVER:** This may also impact the quality of staff at other movie studios as the game appears to make all staff "free agents" when the file is created by the game, and then assigns them at random as the game progresses (This is being investigated to confirm this theory). 
* **RECOMMENDED:** I recommend you wait until you have casting office and the ability to hire all staff types before running this script.

## 🪟 Installing Python on Windows (via official installer)

1. Go to the official [Python downloads page](https://www.python.org/downloads/).
2. Click **Download Python 3.x.x** for Windows.
3. Run the downloaded `.exe` installer.
4. **Important:** Before clicking **Install Now**, check the box that says: `✅ Add Python 3.x to PATH`
5. After installation, verify Python is installed by opening **Command Prompt** and running: `python --version`. You should see something like Python 3.x.x.
