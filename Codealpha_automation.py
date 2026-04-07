import os

# Folder where files create
folder_name = "Automated_files"

# Create folder if not exists
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
print(f" Floder '{folder_name}' ready!")

#Number of files to create
num_files = 5

# Loop to create the files
for i in range(1, num_files + 1):
    file_name = f"file_{i}.txt"
    file_path = os.path.join(folder_name, file_name)
   
   # Write content to file
    with open(file_path, "w") as f:
     f.write(f"this is automated file number {i}\n")
     f.write("This file is created using python automation script.\n")
    print(f"created {file_name}")

# List all files amd their size
print("\n Summary of files:")
for file in os.listdir(folder_name):
    file_path = os.path.join(folder_name, file)
    size = os.path.getsize(file_path)
    print(f"{file} - Size: {size} bytes")