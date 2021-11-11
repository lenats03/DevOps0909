def my_function(current_name):
    print("hello " + current_name)


my_function("lena")


def is_prime() -> bool:
    inp_number = None
    while True:
        try:
            inp_number = int(input("pick a number \n"))
            assert 1<=inp_number<=3
            break

        except TypeError:
            print("Error: enter an integer")
            continue
        except ValueError:
            print("Error: enter a valid integer")
            continue
        except AssertionError ("Please choose a number between 1 and 3")
    for i in range(1, abs(inp_number)):
        if inp_number == 0:
            return True
        if inp_number % i == 0 and i not in (1, abs(inp_number)):
            return False
    else:
        return True