import os
import shutil

fromDir = "G:/Downloads"
toDir = "C:/Users/tj811/OneDrive/Documents/Projects/Python/projects/Project 102/"

filesList = os.listdir(fromDir)

for file in filesList:

    name, extension = os.path.splitext(file)

    if extension == '':
        continue

    if extension in ['.txt','.doc','.pdf','.docx']:

        # original path of file
        path1 = fromDir + '/' + file

        # path of destination directory
        path2 = toDir + '/' + 'Document_Files'

        # final path of file
        path3 = path2 + '/' + file

        # check if destination directory exists and move file
        if os.path.exists(path2):
            print("Moving " + file + '...')
            shutil.move(path1, path3)
        
        # if destination directory didn't exist, create it then move file
        else: 
            os.makedirs(path2)
            print("Moving " + file + '...')
            shutil.move(path1, path3)
        


