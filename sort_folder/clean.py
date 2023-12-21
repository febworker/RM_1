import os
import shutil
import unicodedata

def normalize(filename):
    normalized_name = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('utf-8')
    normalized_name = ''.join(['_' if not c.isalnum() else c for c in normalized_name])
    return normalized_name

def sort_folder(folder_path):
    categories = {
        'images': ['jpeg', 'jpg', 'png', 'svg'],
        'videos': ['avi', 'mp4', 'mov', 'mkv'],
        'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
        'audio': ['mp3', 'ogg', 'wav', 'amr'],
        'archives': ['zip', 'gz', 'tar']
    }
    unknown_extensions = set()

    if not os.path.exists(folder_path):
        print(f"Error: The specified folder '{folder_path}' does not exist.")
        return list(categories.keys()), list(unknown_extensions)

    try:
        for category in categories:
            category_path = os.path.join(folder_path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)  # Create the category folder if it doesn't exist
                print(f"Warning: Folder for category '{category}' did not exist and has been created.")

            print(f"{category}:")
            for file in os.listdir(category_path):
                print(f"  - {file}")

    except Exception as e:
        print(f"Error: {e}")

    return list(categories.keys()), list(unknown_extensions)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    categories, unknown_extensions = sort_folder(folder_path)

    print("\nUnknown extensions:")
    for ext in unknown_extensions:
        print(ext)
