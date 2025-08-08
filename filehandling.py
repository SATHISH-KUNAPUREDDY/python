#1.Practice CRUD Operations on File handling

#  Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Day 6 of my Python learning journey!\n")

# Appending new content
with open("sample.txt", "a") as file:
    file.write("Adding another line using append mode.\n")

#  Reading the file content
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
    
#Delete the file content
with open("sample.txt", "w") as file:
 pass
print("File content deleted successfully!")

# 2. Research on methods flush() and write()

# write() in Python
# Function: Writes data to a file buffer, not necessarily directly to disk.
#flush() in python
# When you're writing logs or streaming output and want the data saved instantly.
# To prevent data loss if a crash happens before the file is closed.
# For real-time file writing (e.g., logs being tailed).