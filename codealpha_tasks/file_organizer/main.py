import os
import shutil

files = os.listdir("images")
os.makedirs("jpg_files", exist_ok= True)

for file in files:
    if file.endswith(".jpg"):
        shutil.move("images/"+file, "jpg_files/"+file)

    else:
        continue    

