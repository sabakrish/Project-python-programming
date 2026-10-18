import os  # import os module to interact with the operating system
import shutil  # import shutil module to move files

FOLDER_CATEGORIES = {
    'Images': ["jpg", "jpeg", "png", "gif"],
    'Documents': ["pdf", "docx", "txt", "xlsx", "pptx", "doc", "xls", "ppt"],
    'Videos': ["mp4", "avi", "mov", "rm"],
    'Music': ["mp3", "wav"],
    'Archives': ["zip", "rar"],
    'Scripts': ["py", "sh"],
}  # 'Others' is handled as the fallback for any extension not listed above


def move_to_category(item_path, item, file_extension, source_folder_path):
    """Move a single file into its matching category folder (or 'Others')."""
    category = 'Others'
    for cat, extensions in FOLDER_CATEGORIES.items():  # find a matching category
        if file_extension in extensions:
            category = cat
            break

    dest_folder = os.path.join(source_folder_path, category)  # destination folder path
    if not os.path.exists(dest_folder):  # create it if missing
        os.makedirs(dest_folder, exist_ok=True)

    shutil.move(item_path, dest_folder)  # move the file to the destination folder
    print(f"Moved file: {item} -> {category}/")


def organize_by_extension(source_folder_path):
    items = os.listdir(source_folder_path)  # list all files and folders in the source folder
    for item in items:  # iterate through each item
        item_path = os.path.join(source_folder_path, item)  # full path of the item

        if os.path.isfile(item_path):  # it's a file: categorize and move it
            filename, file_extension = os.path.splitext(item)  # split filename and extension
            file_extension = file_extension.lower().replace(".", "")  # normalize extension
            move_to_category(item_path, item, file_extension, source_folder_path)
        elif os.path.isdir(item_path):  # skip folders that already exist (e.g. 'Images')
            print(f"Skipping folder: {item}")
        else:
            print(f"Skipping unrecognized item: {item}")


if __name__ == "__main__":
    source_folder_path = input("Enter the folder path to organize files: ").strip()

    if not os.path.isdir(source_folder_path):
        print(f"'{source_folder_path}' is not a valid folder path.")
    else:
        organize_by_extension(source_folder_path)
        print("File organization complete.")
