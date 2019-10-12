# goal is to move files from sub folder to new folder

import shutil
import os

number = 501
destination = "Z:\\DVDs\Music"
back = "\\"

while number < 601:
    source1 = "Z:\\DVDs\Music\Tatort E0" + str(number) + "-share-online.biz"
    source = os.listdir("Z:\\DVDs\Music\Tatort E0" + str(number) + "-share-online.biz")
    for files in source:
            path = source1 + back + files
            print (path)
            shutil.move(path, destination)
    number += 1

