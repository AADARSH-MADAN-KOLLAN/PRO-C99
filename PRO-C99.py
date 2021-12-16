import time
import os
import shutil


def CleanFolder():
    path = input("Enter path of folder to clean: ")
    days = input("Enter the number of days' files to keep (the files before said number of dates will be DELTED) : ")
    deleted_folder_count = 0
    deleted_files_count = 0
    dTime = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if dTime >= GetFileAge(root_folder):
                RemoveFolder(root_folder)
                deleted_folder_count += 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if dTime >= GetFileAge(folder_path):
                        RemoveFolder(folder_path)
                        deleted_folder_count += 1

                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if dTime >= GetFileAge(file_path):
                        RemoveFile(file_path)
                        deleted_files_count += 1
    else:
        print("The entered path does not exist. Please try again.")


def GetFileAge(path):
    ctime = os.stat(path).st_ctime
    return ctime


def RemoveFile(path):
    if not os.remove(path):
        print("Path is removed successfully")
    else:
        print("Unable to delete the path")


def RemoveFolder(path):
    if not shutil.rmtree(path):
        print("Folder removed successfully")
    else:
        print("Unable to delete folder")


CleanFolder()
