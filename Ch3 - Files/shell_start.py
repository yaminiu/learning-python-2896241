#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt.bak"):
        # get the path to the file in the current directory
      
        
        # let's make a backup copy by appending "bak" to the name

        
        # rename the original file

        # now put things into a ZIP archive

        # more fine-grained control over ZIP files

      
if __name__ == "__main__":
    main()
