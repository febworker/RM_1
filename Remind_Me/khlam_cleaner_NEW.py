import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def move_file(file_path, destination_folder):
    
    try:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        os.rename(file_path, destination_path)
        print(f"Moved {file_name} to {destination_folder}")
    except Exception as e:
        print(f"Error moving {file_name}: {e}")

def process_directory(directory):
    
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                
                _, file_extension = os.path.splitext(item)
                
                destination_folder = os.path.join(directory, file_extension[1:])

                # create destination folder

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # moving file to the right folder
                    
                move_file(item_path, destination_folder)
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")

def main(root_folder):
    # list directories
    directories = [str(path) for path in Path(root_folder).rglob("*") if path.is_dir()]
    # execute
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process_directory, directories)

if __name__ == "__main__":
    root_folder = Path("C:/Users/oksan/OneDrive/Робочий стіл/Backgrounds/")  # path can be changed if you need to sort another folder
    main(root_folder)