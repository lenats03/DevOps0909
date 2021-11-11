from functools import reduce

# a

x = 10
y = 20

if x > y:
    print("BIG")
elif x < y:
    print("small")
else:
    None

# b
for i in range(5):
    print(i)

# c
# seasons={1:"summer",2:"fall",3:"winter",4:"spring"}
for i in range(1, 5):
    # print (seasons[i])
    if i == 1:
        print("summer")
    if i == 2:
        print("fall")
    if i == 3:
        print("winter")
    if i == 4:
        print("spring")

# d
# runs 10 times , prints numbers from 1 to 10
count = 1
while count < 11:
    print(count)
    count = count + 1

# e

age = 42
first_letter_last_name = 'L'
currency = 3.25
flew_abroad = True
apt_number = 4

print(age, first_letter_last_name, currency, flew_abroad, apt_number)
print(age + currency)


# f

print("phone number", input("what's your phone number?\n"))


# g

def print_hello():
    print("Hello!")


def calculate():
    print(5 + 3.2)


print_hello()
calculate()


# h

def print_name(name):
    print(name)


def div_by_two(num):
    print(num / 2)


print_name("Lena")
div_by_two(3.25)


# i

def add_nums(a, b):
    return a + b


def add_strings(a, b):
    return a + ' ' + b


print(add_nums(3, 4.5))
print(add_strings("aa", "bb"))

# k
for i in range(1, 6):
    print('#' * i)

# l
max_range = 7
for i in range(max_range):
    result = ""
    for j in range(max_range):
        result = result + ("x" if i == j or j == max_range - i - 1 else " ")
    print(result)


# m


def sum_of_digits() -> int:
    inp_number = None
    while True:
        try:
            inp_number = input("pick a number \n")
            is_int_chk=int(inp_number)
            break
        except TypeError:
            print("Error: enter an integer")
            continue
        except ValueError:
            print("Error: enter a valid integer")
            continue

    res = reduce((lambda x, y: int(x) + int(y)), list(inp_number))
    return res


print("the sum of digits is " + str(sum_of_digits()))
