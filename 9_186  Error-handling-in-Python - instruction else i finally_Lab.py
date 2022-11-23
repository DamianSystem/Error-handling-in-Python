import os
import sys
input_user = input('Acceptable price of a new course idemy. Your price? ')
filepath = input('Enter the path to the file: ')

try:
    line = input_user
    file = open(filepath, 'w')
    file.write(line)
    file.close()
except:
    print("SORRY - WE HAVE AN ERROR", sys.exc_info())
