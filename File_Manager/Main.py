import os

list_dir = os.listdir(".")
list_dir =[each.upper() for each in list_dir]
if len(list_dir) == 1:
    print("This folder looks like Empty")

ext_file = []
folder_name = []
created_folder= {}

for i in list_dir:
    if os.path.isfile(i):
        if i == 'Main.py' or i == "File-Manager.exe":
            continue
        temp = i.split('.')
        ext_file.append(temp[-1])
        created_folder[temp[-1]] = 0
    else:
        list_dir.remove(i)

for i in ext_file:
    if created_folder[i] == 0:
        folder_name.append(f"{i}_files")
        os.mkdir(f"{i}_files")
        created_folder[i] = 1

for each in list_dir:
    temp = each.split(".")
    if temp[-1] not in ext_file:
        continue
    os.rename(each,f"./{temp[-1]}_files/{each}")
