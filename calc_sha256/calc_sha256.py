import sys
import os
import hashlib
import shutil

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # fpath = os.getcwd() + os.sep + sys.argv[1]
        fpath = sys.argv[1]
        if os.path.exists(fpath):
            f = open(fpath, 'rb')
            hash = hashlib.sha256()
            hash.update(f.read())
            f.close()
            hashLast6 = hash.hexdigest().upper()[len(hash.hexdigest())-6:]
            newName = sys.argv[1].rpartition('.')[0] + '_' + hashLast6 + '.' + sys.argv[1].rpartition('.')[2]
            shutil.copy(fpath, 'tmp')
            os.rename('tmp', newName)
            # print(sys.argv[1])
            # print(hash.hexdigest())
            # print(hashLast6)
            # print(newName)
            # os.system("pause")
