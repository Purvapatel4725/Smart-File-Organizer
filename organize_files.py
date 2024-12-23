import os
import shutil
import logging
from tqdm import tqdm  # For progress bar

# Configure logging
logging.basicConfig(filename='organize_files.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Define file categories and their associated extensions
FILE_CATEGORIES = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Scripts": [".py", ".sh", ".bat", ".js", ".html", ".css", ".php"],
    "Others": []  # Files that do not fit into any category
}

def get_user_os():
    while True:
        print("Select your OS:")
        print("1. Windows")
        print("2. Linux")
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            return "windows"
        elif choice == "2":
            return "linux"
        else:
            print("Invalid input. Please enter 1 or 2.")

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def determine_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"

def preview_organization(directory):
    print("\nPreview of the organized folders:")
    file_preview = {category: [] for category in FILE_CATEGORIES.keys()}
    file_preview["Others"] = []

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file_name)
        extension = extension.lower()
        category = determine_category(extension)
        file_preview[category].append(file_name)

    for category, files in file_preview.items():
        if files:
            print(f"{category} ({len(files)} files):")
            for file in files:
                print(f"  - {file}")
    print()
    return file_preview

def organize_files(directory, dry_run):
    script_name = os.path.basename(__file__)
    summary = {category: 0 for category in FILE_CATEGORIES.keys()}
    summary["Others"] = 0

    file_list = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)) and file != script_name]

    for file_name in tqdm(file_list, desc="Organizing files", unit="file"):
        try:
            file_path = os.path.join(directory, file_name)
            _, extension = os.path.splitext(file_name)
            extension = extension.lower()

            category = determine_category(extension)
            category_folder = os.path.join(directory, category)

            if not dry_run:
                create_folder(category_folder)
                shutil.move(file_path, os.path.join(category_folder, file_name))
                logging.info(f"Moved '{file_name}' to '{category}' folder.")
            
            summary[category] += 1
        except Exception as e:
            logging.error(f"Error moving file '{file_name}': {e}")

    return summary

def main():
    user_os = get_user_os()

    if user_os == "windows":
        default_directory = os.getcwd()
    elif user_os == "linux":
        default_directory = os.getcwd()

    custom_directory = input(f"Enter the directory to organize (press Enter to use current directory: {default_directory}): ").strip()
    if custom_directory:
        directory_to_organize = custom_directory
    else:
        directory_to_organize = default_directory

    print(f"Directory to organize: {directory_to_organize}")

    dry_run_input = input("Do you want to perform a dry run? (yes/no): ").strip().lower()
    dry_run = dry_run_input == "yes"

    file_preview = preview_organization(directory_to_organize)

    if dry_run:
        print("Dry run complete. No files were moved.")
        return

    confirm = input("Do you want to proceed with organizing the files? (yes/no): ").strip().lower()
    if confirm == "yes":
        summary = organize_files(directory_to_organize, dry_run=False)
        print("\nOrganization complete. Summary:")
        for category, count in summary.items():
            print(f"{category}: {count} files")
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()
