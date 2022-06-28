

def main():
    print("LOC Python")
    file_name = input("Enter Python file Name: ")
    # check file exist and it is a python file or not
    file = check_file_ex_py(file_name)
    answer = normalize_content(file)
    print(answer)




def check_file_ex_py(file):
    """ check file is python file and try to read content of it """
    # first check its a python file
    if ".py" in file.lower():
        # now validate is python file is exist
        try:
            with open(file) as file_py:
                # read each line of file
                file_inside = file_py.readlines()
        except FileNotFoundError:
            print("File Does Not Exists")
            exit(1)
    else:
        print("Not a python File")
        exit(1)

    return file_inside



def normalize_content(file):
    """Normalize file remove all white space and comment"""

    counter = 0
    for each in file:
        if each.strip() == "":
            continue
        if each.strip().startswith("#"):
            continue
        else:
            counter += 1

    return counter

if __name__ == "__main__":
    main()