# 
# This Python script will backup directorys in source_names
# to the backup_dir directory
# 
# by czchc 20170728
# 

# put the names of directorys you want to archive here
source_names = [ 'sample-dir-A', \
                 'sample-dir-B', \
                 'abccc']

# the name of the backup directory
backup_dir = 'Backup'

####################################################################
###############  No need to modify things below this ###############
####################################################################

import os
import time
import shutil

target_dir  = '.' + os.sep + backup_dir
today_dir = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

source = []
for i in source_names:
    if os.path.exists('.' + os.sep + i):
        source.append('.' + os.sep + i)
    else:
        print("Directory", i, "does not exist")

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("Successfully created directory", target_dir)

if not os.path.exists(today_dir):
    os.mkdir(today_dir)
    print("Successfully created directory", today_dir)

for i in source:
    print("Archiving directory", i)
    target_name = i.rpartition(os.sep)[2]
    file_name = today_dir + os.sep + target_name + '_' + now
    shutil.make_archive(file_name, 'zip', '.', '.' + os.sep + target_name)

# Pause to see the logs, comment this if you don't want
input("Done, press ENTER to exit.")
