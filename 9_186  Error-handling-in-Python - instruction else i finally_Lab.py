import os
import sys
input_user = input('Acceptable price of a new course idemy. Your price? ')
filepath = input('Enter the path to the file: ')

try:
    line = input_user
    file = open(filepath, 'w')
    file.write(line)
    value = int(line)
    file.close()
    print('The value saved in file is', value)
except FileNotFoundError as e:
    print("Error opening file in %s " % filepath, e)
except:
    print("SORRY - WE HAVE AN ERROR", sys.exc_info())
