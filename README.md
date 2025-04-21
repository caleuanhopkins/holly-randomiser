# Hollywood Animal - Free Agents Randomiser

A simple script to help introduce more character randomisation with Weappy's upcoming [Hollywood Animal](https://weappy-studio.com/hollywood-animal/) strategy game. 

<!-- Pytest Coverage Comment:Begin -->
<!-- Pytest Coverage Comment:End -->

<a href="https://www.buymeacoffee.com/caleuanhopkins"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=caleuanhopkins&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

## 🔧 What It Does

### 📖 TLDR
Currently in the game's pre-release state, the character randomisation when new games start are limited especially in important in-game post production roles. This script is designed to help bring a little bit more balance in these roles but also provide freshness when re-rolling new games.

### 💻 Techy Details

For each object where:
- `$type` is `"Data.GameObject.Character.TalentData, Assembly-CSharp"`, **and**
- `"state"` is `0` - correct identifier for if a character is a free agent (shoutout to @skripped on Discord for this!)
- `"id"` is **not** `16` - This is the ID for Lydia Globe and their rating and limit has been fixed since patch 0.8.13EA so we don't want to update them

It will:
- Randomly update each value in the `"professions"` dictionary to a float between **0.1** and **0.99**
- Set `"limit"` to a float between the highest `"professions"` value and **0.99**
- Set `"selfEsteem"` to a float between **-0.9** and **0.9**, biased toward values between **-0.3** and **0.4**

---

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

## 🛠️ Development
**Running Tests**
1. Install development requirements (if you haven't already):
   ```
   pip install -r dev-requirements.txt
2. Run all tests using pytest:
   ```
   pytest
   ```
   This will automatically discover and run any test files that follow the pattern test_*.py.
3. **Optional: Run with coverage report** (if using pytest-cov):
   ```
   pytest --cov
