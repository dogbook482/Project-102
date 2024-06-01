import os
import shutil

from_dir = "C:\\Users\\satya\\OneDrive\\Desktop\\Geethika\\Code\\Python\\Project_102\\Download_Files"
to_dir = "C:\\Users\\satya\\OneDrive\\Desktop\\Geethika\\Code\\Python\\Project_102\\Document_Files"
list_of_files = os.listdir(from_dir)

for fileName in list_of_files:
    root, extension = os.path.splitext(fileName)
    print(root)
    print(extension)

    if(extension==""):
        continue

    if extension in [".docx",".txt",".pdf",".doc"]:
        path1 = from_dir+"\\"+fileName
        path2 = to_dir+"\\"+"Document_Files"
        path3 = to_dir+"\\"+"Document_Files"+"\\"+fileName

        if os.path.exists(path2):
            print("Moving"+fileName+".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving"+fileName+".....")
            shutil.move(path1,path3)