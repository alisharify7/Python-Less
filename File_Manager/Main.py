import os


# get all list of correct directory
list_dir = os.listdir(".")

ext_file = []
folder_name = []
created_folder= {}

# add all file extensions to list
for i in list_dir:
    # check is file or dir
    if os.path.isfile(i):
        # if equal to script name skip
        if i == 'temp.py':
            continue
        # # split file name to catch extension name
        false_temp , temp = i.split('.')
        # append extension of file to ext_file list
        ext_file.append(temp)
        # set folder status to 0
        created_folder[temp] = 0

# create folder for each type 
for i in ext_file:
    # check if folder create status is false
    if created_folder[i] == 0:
        # added folder created name to folder_name list
        folder_name.append(f"{i}_files")
        # create folder
        os.mkdir(f"{i}_files")
        print(f"Now creating this folder = {i}")
        # set status of folder created to 1
        created_folder[i] = 1

# move files to each folder
for each in list_dir:
    temp = each.split(".")
    # if file is create while program run or 
    # create not folder to file name skip it 
    if temp[1] not in ext_file:
        continue
    os.rename(each,f"./{temp[1]}_files/{each}")