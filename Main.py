import os
import shutil
import urllib.request

SubFolders = []

ImageLink = input("Choose an image url or type d for default: ")
if ImageLink == "d":
    ImageLink = "http://i.kinja-img.com/gawker-media/image/upload/s--pgoQB_r6--/c_scale,f_auto,fl_progressive,q_80,w_800/1394453911150307111.jpg"

ImageName = input("Choose an image name or type d for default: ")
if ImageName == "d":
    ImageName = "Beypazari.png"

BaseDir = input("Choose a directory or type d for default: ")
if BaseDir == "d":
    BaseDir = "C://users//"

def download_image():
    print("Downloading the image...")
    global ImageLink
    global ImageName
    urllib.request.urlretrieve(ImageLink,ImageName)

def find_directories():
    global BaseDir
    global SubFolders
    print("Looking for directories...")
    SubFolders = [f.path for f in os.scandir(BaseDir) if f.is_dir()]
    print(SubFolders)

def copy_images():
    print("Copying image to directories...")
    global SubFolders
    global ImageName
    for dir in SubFolders:
        shutil.copyfile(ImageName, "{}/{}".format(dir, ImageName))
        print('File created in {}.'.format(dir))

def cleaning_up():
    print("Cleaning up")
    global ImageName
    os.remove(ImageName)

download_image()
find_directories()
copy_images()
cleaning_up()

