from argparse import FileType
from utils import imgRename, makeImgObjArray
import re


def bulkRename(PATH, template):
    imgObjArray = makeImgObjArray(PATH)
    if "#" in template:    
        for count, image in enumerate(imgObjArray, start=1):
            filetype = image.name
            re.sub(r'^.*?.', ".", filetype)
            imgRename(PATH, image.name, template.replace("#", count))            
    else: 
        for count, image in enumerate(imgObjArray, start=1):
            imgRename(PATH, image.name, "{0}_{1}".format(template, count))