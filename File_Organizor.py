
import os #import os module to interact with the operating system
import shutil #import shutil module to move files

folder_selected=input("Enter the folder path to organize files: ")
source_folder_path = folder_selected #specify the source folder path

new_folder_categories = {
     'Images':["jpg","jpeg","png","gif"],
     'Documents':["pdf","docx","txt","xlsx","pptx","doc","xls","ppt"],
     'Videos':["mp4","avi","mov","rm"],
     'Music':["mp3","wav"],
     'Archives':["zip","rar"],
     'Scripts':["py","sh"],
     'Others':[""]} #list of folder categories

print(new_folder_categories)

def organize_by_extension():
    items=os.listdir(source_folder_path) #list all files and folders in the source folder
    for item in items: #iterate through each item
            item_path = os.path.join(source_folder_path, item) #create full path of the item
            if os.path.isfile(item_path): # check if the item is a file
                 print(f"this is a file",{item})
                 filename, file_extension = os.path.splitext(item) #split the filename and extension
                 file_extension= file_extension.lower().replace(".","") #convert the file extension to lowercase for consistency
                 print(f"filename: {filename}, file_extension: {file_extension}")

                 #match file extension to folder category and move the file
                 for category, extensions in new_folder_categories.items(): #iterate through each category and its extensions
                         if file_extension in extensions:
                             dest_folder = os.path.join(source_folder_path, category) #create destination folder path based on category
                            #if folder does not exist, create it
                             if not os.path.exists(dest_folder): #if destination folder does not exist
                                 os.makedirs(dest_folder, exist_ok=True) #create the destination folder    

                             shutil.move(item_path, dest_folder) #move the file to the destination folder
                             print(f"Moved file: {item} to folder: {category}")
                             break
            #check if the item is a folder
            elif os.path.isdir(item_path):
                 print(f"this is a folder",{item})
            else:
                 print(f"this is something else",{item})

if __name__ == "__main__":
    organize_by_extension()
    print("File organization complete.")
