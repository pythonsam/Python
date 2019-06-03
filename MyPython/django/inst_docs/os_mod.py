
import os

# Get current working directory
cur_dir = os.getcwd()
print("Current directory is %s"%cur_dir)

# List all files in a directory
files_ = os.listdir(".")
print("Files in directory %s are:"%cur_dir)
for file in files_:
    print(file)

new_dir = cur_dir + "\\new_dir"
# Check if a particular path/file exists
if not os.path.exists(new_dir):
    # Create a directory
    os.mkdir(new_dir)

new_inner_dir = new_dir + "\\inner_dir"
if not os.path.exists(new_inner_dir):
    os.mkdir(new_inner_dir)

# Change directory to another location
os.chdir(new_inner_dir)
print("After change of dir, location is %s:"%os.getcwd())

fobj = open("a1.txt", "w");fobj.close()
fobj2 = open("a2.txt", "w");fobj2.close()

print("Files in this dir is %s"%os.listdir("."))
# Remove a file
os.remove("a2.txt")
os.remove("a1.txt")
print("Deleted file a1.txt and a2.txt")

# Remove a directory
os.chdir("..") # Move one directory upward
print("\nFiles/Dirs before removing: %s"%os.listdir()) # Available directories
for file_or_dir in os.listdir():
    if os.path.isfile(file_or_dir):
        os.remove(file_or_dir)
    else:
        os.rmdir(file_or_dir)
print("Files after removing %s\n"%os.listdir())

fobj = open("a1.txt", "w");fobj.close()
# Rename a file
print("Renaming file a1.txt")
os.rename("a1.txt","a1_renamed.txt")
