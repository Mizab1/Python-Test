import os

name = open("folder_name", 'r')
parent_dir = './test'
new_dir = './test/'
for text in name:
    new_folders = text.replace("\n", "")
    os.chdir('./test')
    os.mkdir(new_folders)

    os.chdir(new_folders)
    file_name = new_folders + ".properties"
    file = open(file_name, "w")
    file.write("skins.2=2\nname.2=iregex:(Unspeakable|.* g1)")
    os.chdir('../..')