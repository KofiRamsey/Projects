import zipfile
import os

folder_path = 'D:\\New folder'

for filename in os.listdir(folder_path):
    if filename.endswith('.zip'):  # Check if file is a zip file
        file_path = os.path.join(folder_path, filename)
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(folder_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)  # Create the new folder
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(folder_path)
