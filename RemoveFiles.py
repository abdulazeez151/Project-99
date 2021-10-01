import os 
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = "Path To Delete"

    days = 30

    seconds = time.time() - (days * 24 * 60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):
                remove_folders(root_folder)
                deleted_folders_count += 1

                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)

                    if seconds >= get_file_or_folder_age(path):
                        remove_files(folder_path)
                        deleted_folders_count += 1
                
                for file in files:
                    file_path = os.path.join(root_file,file)

                    if seconds >= get_file_or_folder_age(path):
                        remove_files(file_path)
                        deleted_files_count += 1

        else:

            if seconds >= get_file_or_folder_age(path):
                remove_files(path)
                deleted_files_count += 1

    else:

        print(f'"{path}" is not found')
        deleted_files_count += 1

        print(f'Total Folders Deleted: {deleted_folders_count}')
        print(f'Total Files Deleted: {deleted_files_count}')

def remove_folder(path):

    if not shutil.rmtree(path):
        print(f"{path} is remover successfully")

    else:
        print("Unable to delete the" + path)

def remove_file(path):

    if not shutil.rmtree(path):
        print(f"{path} is remover successfully")

    else:
        print("Unable to delete the" + path)

def get_file_or_folder_age(path):

    ctime = os.stat(path).st_ctime

    return ctime

if __name__== '__main__':
    main()