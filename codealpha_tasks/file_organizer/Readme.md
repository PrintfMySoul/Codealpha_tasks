# Image File Organizer (JPG Auto-Mover)

A simple Python automation script that scans a source folder for `.jpg` image files and automatically moves them into a dedicated destination folder.

## Project Goal

Automate the repetitive task of organizing image files within a file system to improve directory organization and workflow efficiency.

## Features

* **Automatic Folder Creation**: Automatically creates the target directory (`jpg_files`) if it does not already exist.
* **File Filtering**: Identifies and selects files based on the `.jpg` extension.
* **Cross-Platform File Moving**: Moves identified image files from the source directory (`images/`) to the target directory (`jpg_files/`).

## Project Structure

```text
.
├── images/           # Source folder containing unorganized files
├── jpg_files/        # Destination folder where .jpg files are moved
└── main.py           # Python automation script
```

## How to Run

### Prerequisites

* Python 3.x installed on your system.

### Steps

1. Create a folder named `images` in the same directory as the script and place your files inside it.
2. Run the Python script:

```bash
python main.py
```

3. Open the newly created `jpg_files` folder to see your organized `.jpg` files.

## Code Overview

```python
import os
import shutil

# List all files in the source directory
files = os.listdir("images")

# Ensure target directory exists
os.makedirs("jpg_files", exist_ok=True)

# Loop through files and move .jpg images
for file in files:
    if file.endswith(".jpg"):
        shutil.move("images/" + file, "jpg_files/" + file)
```

## Key Concepts Used

* **`os` Module**: Directory listing (`os.listdir`) and directory creation (`os.makedirs`).
* **`shutil` Module**: High-level file operations (`shutil.move`) to transfer files safely.
* **Control Flow & String Methods**: Loop through directory contents and evaluate extensions using `.endswith()`.