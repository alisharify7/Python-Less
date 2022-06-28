def main():
    print("LOC Python")
    file_name = input("Enter Python file Name: ")
    file = check_file_ex_py(file_name)
    answer = normalize_content(file)
    print(answer)


def check_file_ex_py(file):
    """ check file is python file and try to read content of it """
    if ".py" in file.lower():
        try:
            with open(file) as file_py:
                file_inside = file_py.readlines()
        except FileNotFoundError:
            print("File Does Not Exists")
            exit(1)
    else:
        print("Not a python File")
        exit(1)
    return file_inside


def normalize_content(file):
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
    
