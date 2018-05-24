from pathlib import Path
import os


# Check if a given file exists or not
def file_exists(file_path):
    file_path = str(file_path).strip()
    return os.path.isfile(file_path) or Path().is_file(file_path)


# Check if a given directory/folder exists or not
def directory_exists(dir_path):
    return os.path.exists(dir_path)




