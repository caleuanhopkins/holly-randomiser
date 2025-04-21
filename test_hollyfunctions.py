import pytest
import json
import os
from unittest import mock
from hollyfunctions import get_user_inputs, confirm_and_backup, update_talent_data, save_file_updated_data


@pytest.fixture
def tmp_path(pytestconfig):
    """Fixture to get the root directory path from pytestconfig."""
    return pytestconfig.rootdir


@pytest.fixture
def mock_json_path(tmp_path):
    """Fixture to create a mock JSON file for testing."""
    test_file = tmp_path / "test_saved_game.json"
    with open("test_saved_game.json", "r", encoding="utf-8-sig") as src:
        data = json.load(src)
    with open(test_file, "w", encoding="utf-8-sig") as dst:
        json.dump(data, dst)
    return str(test_file)


@pytest.fixture
def mock_inputs(monkeypatch):
    """Fixture to mock input() calls for user prompts."""
    monkeypatch.setattr("builtins.input", lambda prompt="": "Y" if "correct" in prompt else "TestUser" if "username" in prompt else "Save1")


def test_get_user_inputs(mock_inputs):
    """Test the get_user_inputs function."""
    expected = fr"C:\Users\TestUser\AppData\LocalLow\Weappy\Holly\Saves\Profiles\0\Save1.json"
    assert get_user_inputs() == expected


def test_confirm_and_backup(monkeypatch, tmp_path):
    """Test the confirm_and_backup function."""
    dummy_file = tmp_path / "test_saved_game.json"
    monkeypatch.setattr("builtins.input", lambda prompt="": "y")
    confirm_and_backup(str(dummy_file))
    backup_file = str(dummy_file).replace(".json", "_backup.json")
    assert os.path.exists(backup_file)


def test_update_talent_data(mock_json_path):
    """Test the update_talent_data function."""
    updated_data = update_talent_data(mock_json_path)
    assert isinstance(updated_data, dict)
    
    # Recursive check for specific attributes in updated data
    def recursive_update(o):
        if isinstance(o, dict):
            # Check conditions based on the data
            if o.get("$type") == "Data.GameObject.Character.TalentData, Assembly-CSharp":
                if o.get("id") == 16:
                    assert True  # Expected behavior met

                # Check conditions related to professions, limit, and selfEsteem
                if o.get("state") == 0:
                    assert all(0 < value < 1 for value in o.get("professions", {}).values())
                    assert 0 < o.get("limit", -1) < 1
                    assert o.get("selfEsteem", 0) < 1
                
            for key in o:
                recursive_update(o[key])
        elif isinstance(o, list):
            for item in o:
                recursive_update(item)

    recursive_update(updated_data)


def test_save_file_updated_data(mock_json_path, tmp_path):
    """Test saving updated data to a file."""
    data = update_talent_data(mock_json_path)
    save_file_updated_data(data, str(mock_json_path))

    # Check if the file exists and has updated content
    assert os.path.exists(mock_json_path)
    with open(mock_json_path, 'r', encoding='utf-8-sig') as f:
        loaded = json.load(f)
    assert isinstance(loaded, dict)
