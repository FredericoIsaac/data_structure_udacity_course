import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_list = os.listdir(path)   # returns a list containing the names of the entries in the directory given by path

    # Base Case
    if len(path_list) == 0:  
          return []

    # Create a list that ill have all the path of the files with the suffix
    path_files = [file for file in path_list if "." + suffix in file]
    # Get all the files in the current directory
    path_folders = [file for file in path_list if "." not in file]

    # The recursion call so we go to all the subdirectories
    for folder in path_folders:
          path_files.extend(find_files(suffix, path + "\\" + folder))

    return path_files


## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./pset02\problem2.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))

path_base = os.getcwd() + '\pset02\\testdir'

print (os.path.isfile(path_base))
# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files(suffix='h', path=path_base))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files(suffix='z', path=path_base))
# []