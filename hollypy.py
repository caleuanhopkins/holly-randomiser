from hollyfunctions import get_user_inputs, confirm_and_backup, update_talent_data, save_file_updated_data

# Run script to collect input from users
file_path = get_user_inputs()

# Get file data
data = confirm_and_backup(file_path)

# Run the update
updated_data = update_talent_data(file_path)

#Save the file data
save_file_updated_data(updated_data, file_path)

print(f"✅ File updated successfully: {file_path}")