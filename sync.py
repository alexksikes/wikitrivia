# Author: Alex Ksikes 
import os

cmd = "rsync -Puzav --exclude='config.py' --exclude='.bzr' dana:/wikitrivia/scripts/"
os.system(cmd)
