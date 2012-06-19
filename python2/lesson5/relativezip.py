import os, glob, zipfile

"""Create a project named Python2_Homework05 and add it to the Python2_Homework working set. In this project, write a function that takes a directory path and creates an archive of the directory only. 
    For example, if the same path were used as in the example ("v:\\workspace\\python2_Lesson05\\src\\archive_me"), the zipfile would contain "archive_me\\groucho" "archive_me\\harpo" and "archive_me\\chico."
    The base directory ("archive_me" in the example above) is the final element of the input, and all paths recorded in the zipfile should start with the base directory.
    If the directory contains subdirectories, the subdirectory names and any files in the subdirectories should not be included. 
    (Hint: You can use isfile() to determine if a filename represents a regular file and not a directory.)"""
    
def dirArchive(path):
    basedir = os.path.dirname(path)
    relativedir = os.path.basename(path)
    
    startPath = os.curdir
    os.chdir(basedir)
    
    # Select files to compress
    filenames = glob.glob(os.path.join(relativedir, "*"))
    for fn in filenames:
        if not os.path.isfile(basedir + '\\' + fn):
            filenames.remove(fn)

    # Make archive and compress files
    archive_fn = path + ".zip"
    zf = zipfile.ZipFile(archive_fn, "w")
    for fn in filenames:
        zf.write(fn)
    zf.close()
    
    os.chdir(startPath)