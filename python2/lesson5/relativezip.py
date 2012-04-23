import os, glob, shutil, zipfile

"""Create a project named Python2_Homework05 and add it to the Python2_Homework working set. In this project, write a function that takes a directory path and creates an archive of the directory only. 
    For example, if the same path were used as in the example ("v:\\workspace\\python2_Lesson05\\src\\archive_me"), the zipfile would contain "archive_me\\groucho" "archive_me\\harpo" and "archive_me\\chico."
    The base directory ("archive_me" in the example above) is the final element of the input, and all paths recorded in the zipfile should start with the base directory.
    If the directory contains subdirectories, the subdirectory names and any files in the subdirectories should not be included. 
    (Hint: You can use isfile() to determine if a filename represents a regular file and not a directory.)"""
    
def dirArchive(path):
    basedir = os.path.dirname(path)
    relativedir = os.path.basename(path)

    # Select files to compress
    os.chdir(basedir)
    filenames = glob.glob(os.path.join(relativedir, "*"))
    print(filenames)
    print(basedir)
    for fn in filenames:
        if not os.path.isfile(basedir + '\\' + fn):
            filenames.remove(fn)

    # Make archive and compress files
    archive_fn = path + ".zip"
    print(archive_fn)
    zf = zipfile.ZipFile(archive_fn, "w")
    for fn in filenames:
        zf.write(fn)
    print(zf.namelist())
    zf.close()

filenames = ["groucho", "harpo", "chico"]
path = "v:\\workspace\\Python2_Homework05\\src\\archive_me"

# Make test files to compress
os.mkdir(path)
for fn in filenames:
    f = open(os.path.join(path, fn), "w")
    f.close()
# Make test subdirectory and subdirectory files
os.mkdir(path + "\\subdir")
for fn in filenames:
    f = open(os.path.join(path + "\\subdir", fn), "w")
    f.close()

# Run the directory compression function
startPath = os.curdir
dirArchive(path)
os.chdir(startPath)

# Clean up.
#shutil.rmtree(path)
