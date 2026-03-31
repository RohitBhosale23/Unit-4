# Step 1: Open file in write mode and add content
file = open("data.csv", "w")

file.write("Name,Age,City\n")
file.write("Rohit,19,Pune\n")
file.write("Sapna,20,Pune\n")

file.close()

print("Data written successfully!")

# Step 2: Open file in append mode and add more data
file = open("data.csv", "a")

file.write("Amit,21,Delhi\n")

file.close()  

print("Data appended successfully!")

# Step 3: Open file in read mode and display content
file = open("data.csv", "r")

content = file.read()
print("\nFile Content:\n")
print(content)

file.close()   