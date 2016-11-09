import os
import sys
import shutil
from PIL import Image

width = 0
height = 0
flag = 0


def main(args):
    if len(args) < 2:
        print("Not enough arguments")
        print("Usage: python win10wp.py <username> <path/to/dest>")
        sys.exit()
    user = args[0]
    dest = args[1]
    src = "C:/Users/" + user + "/AppData/Local/Packages/" + \
        "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/" + \
        "LocalState/Assets"
    if not os.path.exists(src):
        print("invalid username")
        sys.exit()
    landscape = "/landscape/"
    portrait = "/portrait/"
    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(dest + landscape):
        os.makedirs(dest + landscape)
    if not os.path.exists(dest + portrait):
        os.makedirs(dest + portrait)
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        dest_file_name = os.path.join(dest, file_name)
        if(os.path.isfile(full_file_name)):
            if(os.path.exists(dest_file_name + '.jpg')):
                os.remove(dest_file_name + '.jpg')
            shutil.copy(full_file_name, dest)
    for file_name in os.listdir(dest):
        full_file_name = os.path.join(dest, file_name)
        if not os.path.isfile(full_file_name):
            continue
        new_file_name = full_file_name + '.jpg'
        os.rename(full_file_name, new_file_name)
    for file_name in os.listdir(dest):
        flag = 0
        full_file_name = os.path.join(dest, file_name)
        if not os.path.isfile(full_file_name):
            continue
        try:
            with Image.open(full_file_name) as im:
                width, height = im.size
        except:
            flag = 1
        if width < 400 or height < 400 or flag == 1:
            os.remove(full_file_name)
        elif width > height:
            if(os.path.exists(dest + landscape + file_name)):
                os.remove(dest + landscape + file_name)
            shutil.move(full_file_name, dest + landscape)
        else:
            if(os.path.exists(dest + portrait + file_name)):
                os.remove(dest + portrait + file_name)
            shutil.move(full_file_name, dest + portrait)

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise "Must be using Python 3"
        sys.exit()
    main(sys.argv[1:])
