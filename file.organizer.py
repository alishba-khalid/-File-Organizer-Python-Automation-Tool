import os
import shutil

# Dictionary to map file extensions to folder names
FILE_TYPES = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
    'Others': []  # For uncategorized files
}

# Function to get the folder name based on file extension
def get_folder_name(file_extension):
    for folder, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return folder
    return 'Others'

# Ask the user for the folder path
folder_path = input("Enter the full path of the folder you want to organize:\n").strip()

# Check if path is valid
if not os.path.exists(folder_path):
    print("\033[91mError: Folder not found. Please check your path.\033[0m")
else:
    print("\n\033[94mOrganizing files...\033[0m\n")

    for file_name in os.listdir(folder_path):
        full_file_path = os.path.join(folder_path, file_name)

        # Skip if it's a folder
        if os.path.isdir(full_file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(file_name)

        # Get the correct folder name for this file
        folder_name = get_folder_name(file_extension)

        # Create the folder if it doesn't exist
        target_folder = os.path.join(folder_path, folder_name)
        os.makedirs(target_folder, exist_ok=True)

        # Move the file
        try:
            shutil.move(full_file_path, os.path.join(target_folder, file_name))
            print(f"\033[92m✔ Moved: {file_name} → {folder_name}\033[0m")
        except Exception as e:
            print(f"\033[91m✖ Error moving {file_name}: {e}\033[0m")

    print("\n\033[96m🎉 All files have been organized successfully!\033[0m")
