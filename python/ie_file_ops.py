import os
import pathlib
#   LINK: https://realpython.com/working-with-files-in-python/

path_data = os.environ.get('mld_data')
path_data_example = os.path.join(path_data, 'example')
print(path_data_example)
print()

#   Open (text) file and read contents:
#   with open(path_file, 'r') as f:
#       data = f.read()

#   Open (text) file and write:
#   data = 'data to be written to file'
#   with open(path_file, 'w') as f:
#       f.write(data)

#   os.listdir()	            Returns a list of all files and folders in a directory (Deprecated)
#   os.scandir()	            Returns an iterator of all the objects in a directory including file attribute information
#   pathlib.Path.iterdir()	    Returns an iterator of all the objects in a directory including file attribute information

entries = os.listdir(path_data_example)
for entry in entries:
    if os.path.isfile(os.path.join(path_data_example, entry)):
        print("file: " + str(entry))
    if os.path.isdir(os.path.join(path_data_example, entry)):
        print("dir: " + str(entry))
print()

entries = os.scandir(path_data_example)
for entry in entries:
    if os.path.isfile(entry):
        print("file: " + str(entry))
    if os.path.isdir(entry):
        print("dir: " + str(entry))
print()

entries = pathlib.Path(path_data_example)
for entry in entries.iterdir():
    if entry.is_file():
        print("file: " + str(entry))
    if entry.is_dir():
        print("dir: " + str(entry))
print()


#   File attributes - size, mtime, <>
#       for os.scandir() results
#       for pathlib.Path.iterdir() results

#   Creating directories
#       os.mkdir()	                Creates a single subdirectory
#       pathlib.Path.mkdir()	    Creates single or multiple directories
#       os.makedirs()	            Creates multiple directories, including intermediate directories


#   filename pattern matching
#       startswith()	                        Tests if a string starts with a specified pattern and returns True or False
#       endswith()	                            Tests if a string ends with a specified pattern and returns True or False
#       fnmatch.fnmatch(filename, pattern)	    Tests whether the filename matches the pattern and returns True or False
#       glob.glob()	                            Returns a list of filenames that match a pattern
#       pathlib.Path.glob()	                    Finds patterns in path names and returns a generator object


#   Traversing Directories and Processing Files
#       os.walk()

#   Making Temporary Files and Directories


#   Deleting Files and Directories
#       os.remove()	                Deletes a file and does not delete directories
#       os.unlink()	                Is identical to os.remove() and deletes a single file
#       pathlib.Path.unlink()	    Deletes a file and cannot delete directories
#       os.rmdir()	                Deletes an empty directory
#       pathlib.Path.rmdir()	    Deletes an empty directory
#       shutil.rmtree()	            Deletes entire directory tree and can be used to delete non-empty directories

#   Copying, Moving, and Renaming Files and Directories

#   Archiving

#   Reading multiple files


