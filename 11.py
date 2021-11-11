# my_file = open("read_my_contents.txt", "r")
# contents = my_file.readlines()
# print(contents)
# for line in contents:
#     print(line, end='')
#
import io

my_file = open("names.txt", 'w')
for i in range(1):
    current_name = input('enter your name: ')
    my_file.write(current_name + '\n')
my_file.close()

try:
    my_file = open("names.txt", 'r')
    for name in my_file.readlines():
        print(f"Hello,{name}", end='')
        try:
            my_file.write(f"Hello,{name}")
        except io.UnsupportedOperation as e:
            print("Cannot access the file")
except FileNotFoundError:
    print("Cannot access the file")
finally:
    1



