EXERCISE 1

1. Import the os module

2. Read the user's information that can be interpreted as a number, e.g. ask for an acceptable purchase price for the next course on Udemy. Remember the result in the line variable

3. Read the path to the file from the user

4. Without any additional control, save the line to a file with the specified path

5. Test the script by specifying the path to a file that can be created (e.g., the path to a non-existent file in an existing directory) and a path that cannot be created (for example, the path to a non-existent file in a non-existent directory). Notice what error is displayed in the second case

EXERCISE 2

1. Modify the previous example so that the instructions that perform operations on the file are in the try block

2. If an error occurs, display the message "SORRY - WE HAVE AN ERROR"

3. Perform tests as before

EXERCISE 3

1. Add a except statement that will catch the FileNotFoundError error:

2. For this specific error, display the message "Error opening file". You can add detailed information about the error

EXERCISE 4

1. As the last statement in the try block, add the conversion of the value stored in the line variable to the int type. Remember the result in the value variable

2. Display the information "The value saved in file is...."

3. Test the program in several ways: a value that converts to a number or not, a path that exists or does not exist, etc.

EXERCISE 5

1. Add another except statement that handles the ValueError error that may be generated during the line to value conversion.

2. For this error, display the message "The value entered cannot be converted to a number". You can view more details about the error

3. Add an else block that displays the message "Actions completed successfully"

4. Test the script by generating various errors