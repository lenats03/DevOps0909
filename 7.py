def my_function(current_name):
    print("hello " + current_name)


my_function("lena")

    print ('Lena')


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
        if i != 0 or i in (1, abs(inp_number)):
            continue
        return False
    else:
        return True

    print('diff for conflict2xxcvxcvs')