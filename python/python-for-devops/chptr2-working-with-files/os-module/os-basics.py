#!/usr/bin/env python3

import os

# List the contents of a directory
mydir = '/home/user/'
mydir_content = os.listdir(mydir)
print(mydir_content)

# Rename a file or directory
src = 'home/user/test__file.txt'
dst = '/home/user/test-file.txt'
os.rename(src, dst)

# Change the permission settings of a file or directory
os.chmod('test-file.txt', 0o777)

# Create a directory
os.mkdir('/tmp/holding')

# Recursively create a directory path
os.makedirs('/tmp/kbehrman/tmp/scripts/devops')

# Delete a file
os.remove('test-file.txt')

# Delete a single directory
os.rmdir('/tmp/holding')

# Delete a tree of directories, starting with the leaf directory and
# working up the tree. The operation stops with the first nonempty directory
os.removedirs('/tmp/kbehrman/tmp/scripts/devops')

# Get stats about the file or directory. These stats include
# st_mode, the file type and permissions, and st_atime, the
# time the item was last accessed
os.stat('os-basics.py')