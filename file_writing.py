# 1) Write a file
file = open("demo_file.txt", "w")

file.write("Hii!\nThis is my new file\n")
file.write("In this file we are going to write information about python\n")

file.close()

print("Data written successfully.\n")

# 2) Reading from the file
file = open("demo_file.txt", "r")

content = file.read()
print("Content of the file:", content)

file.close()

# 3) Appending to the file
file = open("demo_file.txt", "a")

file.write("This is a fourth line.\n")

file.close()

print("Data appended successfully.\n")

# 4) Read updated file
file = open("demo_file.txt", "r")

updated_content = file.read()

print("Updated content of the file:")
print(updated_content)

file.close()