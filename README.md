# Smart File Organizer

Effortlessly organize your files into categorized folders based on their types. The Smart File Organizer is a versatile Python script that works on both Windows and Linux platforms, offering an intuitive way to clean up and manage your directories.

---

## Features

- Automatically detects and organizes files by type (e.g., Videos, Images, Documents, etc.).
- Works seamlessly on **Windows** and **Linux**.
- **Custom Directory Input**: Specify the directory you want to organize.
- **Preview Mode**: Get a dry-run preview of how files will be organized.
- **Post-Organization Summary**: View a detailed report of the organization process.
- **Log File Generation**: All file movements and errors are logged for easy debugging.
- **Error Handling and Recovery**: Handles inaccessible files gracefully.
- **Progress Bar**: Provides real-time feedback during the file organization process.

---

## How It Works

1. **Select Your OS**: Choose between Windows and Linux.
2. **Choose a Directory**: Use the current directory or specify a custom path.
3. **Preview Organization**: See how files will be categorized without making changes.
4. **Confirm and Organize**: Proceed to organize files after previewing.
5. **View Summary**: Get a breakdown of organized files and their categories.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Purvapatel4725/Smart-File-Organizer.git
   cd Smart-File-Organizer
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the script:
   ```bash
   python organize_files.py
   ```

2. Follow the prompts:
   - Select your OS (Windows/Linux).
   - Enter the directory to organize (or press Enter to use the current directory).
   - Optionally preview the organization with a dry run.
   - Confirm to proceed with organizing files.

3. After the process is complete, check the generated folders in the selected directory.

---

## File Categories

The script categorizes files into the following folders:

- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.odt`
- **Spreadsheets**: `.xls`, `.xlsx`, `.csv`
- **Presentations**: `.ppt`, `.pptx`
- **Archives**: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
- **Scripts**: `.py`, `.sh`, `.bat`, `.js`, `.html`, `.css`, `.php`
- **Others**: Files that do not fit into any category

---

## Log File

All file movements and errors are logged in `organize_files.log`. Use this file to review the organization process or troubleshoot issues.

---

## Example Output

**Preview Mode:**
```
Preview of the organized folders:
Videos (2 files):
  - video1.mp4
  - movie.mkv
Images (3 files):
  - image1.jpg
  - photo.png
  - graphic.bmp
Documents (1 file):
  - document.pdf
```

**Post-Organization Summary:**
```
Organization complete. Summary:
Videos: 2 files
Images: 3 files
Documents: 1 file
Others: 0 files
```

---

## Notes

- Ensure you have Python 3.x installed on your system.
- The script excludes itself (`organize_files.py`) from the organization process.
- For best results, run the script in directories with a large number of unorganized files.

---

## Author
**Purva Patel**  

