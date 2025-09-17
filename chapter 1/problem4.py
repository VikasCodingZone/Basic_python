import os

# Get the path of the directory (you can also give a specific path like "C:/Users/YourName/Documents")
directory_path = "/"

# List all files and folders in the directory
content = os.listdir(directory_path)

# Print each item
print("Content of the directory:")
for item in content:
    print(item)
