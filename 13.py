def save_name():
    try:
        name = str(input("your name, please \n"))
        my_file = open("names.txt", 'a')
        my_file.write(name + '\n')
        my_file.close()

    except BaseException:
        print("Error")


def print_names():
    try:
        with open("names.txt", 'r') as my_file:
            for name in my_file.readlines():
                print(f"Hello,{name}", end='')
    except FileNotFoundError:
        print("Cannot access the names  file")


save_name()
print_names()
