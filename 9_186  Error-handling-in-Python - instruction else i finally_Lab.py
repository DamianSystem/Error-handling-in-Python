input_user = input('Acceptable price of a new course idemy. Your price? ')
filepath = input('Enter the path to the file: ')

line = input_user
file = open(filepath, 'w')
file.write(line)
file.close()
