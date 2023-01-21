import os

def parent_directory():
    # Create a relative path to the parent of the current working directory
    # os.chdir('..')
    relative_parent = os.path.join(str(os.getcwd()), str(os.chdir('..')))
   # relative_parent = str(relative_parent)

    # Return the absolute path of the parent directory
    return relative_parent

print(parent_directory())