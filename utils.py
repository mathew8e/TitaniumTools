from PIL import Image
import shutil
from os import listdir
import os

def makeImgObjArray(PATH):
    ArrayWithImgObjects = []
    class ImageObj():
        def __init__(self, name, width, height):
            self.name = name
            self.width = width
            self.height = height
            self.ratio = width/height
                
    for i in listdir(PATH):
        if i.endswith(".png") or i.endswith(".jpg"):
            img = Image.open("{0}/{1}".format(PATH,i))
            w, h  = img.size
            ArrayWithImgObjects.append(ImageObj(i, w, h))
            img.close()
    
    return ArrayWithImgObjects

def imgMove(PATH, name, foldername):
    shutil.move("{0}/{1}".format(PATH, name), "{0}/{1}".format(PATH, foldername))

def imgRename(PATH, name, rename):
    os.rename("{0}/{1}".format(PATH, name), "{0}/{1}".format(PATH, rename))