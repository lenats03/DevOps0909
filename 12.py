def get_user_age():
    input_from_user=int(input("your age please"))
    if input_from_user<0:
        raise ValueError("age can't be negative")
try:
    get_user_age()
except ValueError as e:
    print (str(e.args))