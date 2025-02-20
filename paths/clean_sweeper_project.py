from pathlib import Path
import shutil

# user specify a directory path
# validate

# create new directory ("closet") within user-specified dir
# mkdir

# create 3 more sub directories
# text_files
# csv_files
# folders

# iterate over the user-specified directory
# ensure to exclude the 'closet' directory
# check if file is .txt or .csv
# move into the 'text_files' or 'csv_files' directories
# delete any directory with 'temp' in the name
# if a directory doesn't have 'temp' in the name, move to 'folders' directory
# any remaining files should be moved to the 'closet' directory

## more specific conditions should come before general ones so they are not swept up
# once script has finished, print "folder cleanup complete!"