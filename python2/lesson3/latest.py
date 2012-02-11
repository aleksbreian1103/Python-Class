import glob
import os

"""write a module containing a function to examine the contents of the current working directory and 
    print out a count of how many files have each extension (".txt", ".doc", etc.)"""
    
def print_extension(path="."):
    ext_dict = {}

    files = glob.glob(os.path.join(path, "*"))
    ext_files = [os.path.splitext(fn) for fn in files]
    ext = [ext for (name, ext) in ext_files]

    for each in ext:
        if ext_dict.__contains__(each):
            ext_dict[each] += 1
        else:
            ext_dict[each] = 1

    return ext_dict
