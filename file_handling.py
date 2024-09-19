# file_handling_assignment.py

# Creating a new text file and writing to it
with open('my_file.txt', 'w') as file:
    file.write("This is the first line of the file.\n")
    file.write("Here is a number: 12345\n")
    file.write("And here is another line with some text.\n")

# Reading and displaying the content of the file
print("Contents of 'my_file.txt' after writing:")
with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending additional lines to the file
with open('my_file.txt', 'a') as file:
    file.write("Appending the first additional line.\n")
    file.write("Here is the second additional line.\n")
    file.write("And this is the third additional line.\n")

# Reading and displaying the updated content of the file
print("Contents of 'my_file.txt' after appending:")
with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)
