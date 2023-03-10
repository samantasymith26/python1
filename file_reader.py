filename = input("Enter the name of the file to read: ")
with open(filename, 'r') as file:
    contents = file.read()
    print(contents)
