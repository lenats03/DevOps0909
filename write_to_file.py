
import os
print ('Hello'+ os.environ['name'])
a=open('c:/temp/tempfile.txt' ,'w')
a.write(os.environ['name'])
a.close()