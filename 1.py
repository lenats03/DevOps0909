print('hello world')
a = 'Hello world'
b = 3
c = True
d = ['lena', 21, True]  # list
e = ('moshe', 23, False)  # tuple - immutable
f = {'name': 'lena', 'age': 23, 'isMarried': True, 'hobbies': ['a', 'b']}  # dictionary
# string escape chars: / = ignore the 'special' char, /t tab /n new line /r reverse
print(f.values())

g = f'{a} {a}'
print(g)
gg = '%s %i' % (a, b)
print(gg)

if a == 4:
    print('a is 4')
