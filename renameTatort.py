#rename tatort files to TVDB usance

import shutil, os

startnumber = 686
endnumber = 700
source = os.listdir("Z:\\DVDs\Torrents\Tatort\Tatorttest")
source1 = "Z:\\DVDs\Torrents\Tatort\Tatorttest"
back = "\\"
year = 2008
episode = 1

while startnumber <= endnumber:
    #identify file to change
    for files in source:
        string = str(startnumber)
        if files.find(string) == 1:
            os.rename(source1 + back + files,source1 + back + "Tatort.S" + str(year) + "E" + str(episode) + "." + files[7:])
            print(files[7:])
            print(string)
            break
    startnumber = startnumber + 1
    episode = episode + 1

    #count file name and replace first seven digits with Tatort.SXXXXEXX.
