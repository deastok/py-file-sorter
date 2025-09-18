"""
File Sorter
A simple script to organize files into subfolders based on their type
"""

import os
import sys
import shutil
from pathlib import Path

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".txt"],
    "Music": [".mp3", ".wav"],
    "Video": [".mp4", ".mov", ".wmv", ".webm"],
    "Archives": [".zip", ".rar", ".7z"]
}

def sort_files(folder_path: str):
    base_path = Path(folder_path)

    if not base_path.exists():
        print(f"Folder {base_path} doesn't exist.")
        return

    for file in base_path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()

            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    target_folder = base_path / category
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_folder / file.name))
                    print(f"Moving {file} to {target_folder}")
                    break
            else:
                other_folder = base_path / "Other"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_folder / file.name))
                print(f"Moving {file} to {other_folder}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <folder_path>")
        return

    folder_path = sys.argv[1]
    sort_files(folder_path)

if __name__ == "__main__":
    main()

