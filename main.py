# file = open("my_file")  # A better way to open file and auto close Down Below.
# with open("my_file") as file:
#     content = file.read()
#     print(content)
#     file.close()

# mode=w to write, mode=r to read, mode=a to append. if file doesn't exist while w, file will be created
with open("my_file", "a") as file:
    file.write("\nNew text.")  # We use \n to add new text in a new line.
