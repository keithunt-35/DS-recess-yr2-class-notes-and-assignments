#exercise 1: Create an automation script that backs up files from a folder within 3 minutes fo modification to a backup folder.

import os
import shutil
import time

def backup_recently_modified(source_folder, backup_folder, minutes=1):
    """Backup files modified within the last 3 minutes"""
    current_time = time.time()
    cutoff = current_time - (minutes * 60)
    
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            mod_time = os.path.getmtime(file_path)
            
            if mod_time > cutoff:
                # Created relative path for backup
                relative_path = os.path.relpath(file_path, source_folder)
                backup_path = os.path.join(backup_folder, relative_path)
                
                # Create directories if needed
                os.makedirs(os.path.dirname(backup_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(file_path, backup_path)
                print(f"Backed up: {file_path}")

if __name__ == "__main__":
    SOURCE_FOLDER = "/home/keithunt_35/Desktop"
    BACKUP_FOLDER = "/home/keithunt_35/Desktop/backup"
    
    while True:
        backup_recently_modified(SOURCE_FOLDER, BACKUP_FOLDER)
        time.sleep(60)  # Check every minute