#1
#a = 1/0

#2
try:
    a=1/0
except ZeroDivisionError:
    print ('wrong')


#3

try :
    x = 1
finally :
    print("finally")


#4
#Except:
#All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.

#5
#The exception is too general. Usually we would like to give the specific exceptions a personal treatment and use the non-specific ones at the end of the exception list

#6
#IOError : error in input or output
#Zero division error: exception of dividing by zero

#7-9

my_file = open("textfile.txt", 'a')
for i in range(30):
    for j in range(2):
        my_file.write(chr(i+j+50))
    my_file.write('\n')

my_file.write('Lena\n')
my_file.write('לנה')
my_file.close()

with open("textfile.txt", 'r') as my_file:
    for line in my_file.readlines():
        print (line, end='')94.0.4606.81

#10
from PIL import Image
my_image=Image.new("RGB",(100,100),'blue')
#my_image.show()
my_image.save('image.png','png')









