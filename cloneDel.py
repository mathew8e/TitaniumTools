from PIL import Image
from os import listdir, remove
import numpy as np


#make a progress bar

def loadImages(path):
    # return array of images

    print("Started img loading")
    imagesList = listdir(path)
    loadedImages = []
    for image in range(len(imagesList)):
        try:
            img = Image.open(path + imagesList[image])
        except PermissionError:
            print(" FILE: " + imagesList[image].replace(path,'')+" can't be opened it is proboaly a folder so it cant open it")
            quit()
        loadedImages.append(img)
    print("Finished img loading")
    return loadedImages


def convImgToNpArrays(array):
    #function for creating a np array

    print("Started np converting")
    numpyimg = []
    for i in range(len(array)):
        numpyimg.append(np.asarray(array[i]))
    print("Np convert end")
    return numpyimg

def cloneFind(npimgs, imgs):
    # checking each photo with eachother

    dictOfIndexes = {}
    pairArray = {}

    #two indexes will go through all files
    for imgIndex1 in range(len(npimgs)):
        print("checking",imgIndex1," from ", len(npimgs))
        for imgIndex2 in range(len(npimgs)):

            #                 if imgs are the same                      if the img is not itself            if img clone isnt 2 1  1 2
            if np.array_equal(npimgs[imgIndex1], npimgs[imgIndex2]) and imgIndex1 != imgIndex2 and not(imgIndex1 in dictOfIndexes.values()) and not(imgIndex2 in dictOfIndexes.values()) and not(imgIndex2 in dictOfIndexes.keys()) and not(imgIndex1 in dictOfIndexes.values()):

                img1 = imgs[imgIndex1].filename #.replace(path, '')
                img2 = imgs[imgIndex2].filename #.replace(path, '') #this replaces the path

                # just some debugging
                print("Found ",img1," with ",img2)
                
                
                if img1 in pairArray.keys() :
                    print(pairArray[img1])
                    pairArray[img1].append(img2)
                elif not any([True for k,v in pairArray.items() if img1 in v]):
                    pairArray[img1] = [img2]

                #remembering matched indexes to not repeat itself
                dictOfIndexes[imgIndex1] = imgIndex2
    print("Finished Checking...")


    return pairArray

    #this return statement is funny lol XD return unique values
    #return list(set(cloneImgArrayOfArrays))

def deleteCloneImages(dictOfCloneImages):
    #this function will delete all unoriginal photos
    if (dictOfCloneImages != {}):
        print("Started Deleting...")
        for k,v in dictOfCloneImages.items():
            for delImg in v:
                remove(delImg)
                print(f"removing {delImg} \n")
        return 1
        
    else:
        print("Nothing to remove")
        return "Nothing to remove"
        
def duplicateDelete(PATH):
    path = PATH.replace("\\", "//") + "/"
    imgs = loadImages(path)
    npimgs = convImgToNpArrays(imgs)
    cloneListArray = cloneFind(npimgs, imgs)
    return deleteCloneImages(cloneListArray)
        
                




# '''INSERT PATH HERE TO IMG FOLDER'''

# #-----------------------------------------------------------------------------------------------------------------------------------------

# winpath = r"C:\Users\mathe\Downloads\pictures for the Website 10 11 2021 -20211104T180815Z-001\pictures for the Website 10_ 11_ 2021\Brend alouie\images from a lecture trip at Ningbo University, Ningbo, P.R.China in the Spring 2008" # <----

# #-----------------------------------------------------------------------------------------------------------------------------------------


# path = winpath.replace("\\","//")+"/"

# # images in an regular array
# imgs = loadImages(path)

# # change images to an np array
# npimgs = convImgToNpArrays(imgs)

# cloneListArray = cloneFind(npimgs)


# #print(f"\n        Found these images as copy \n  {cloneListArray}")

            
# deleteCloneImages(cloneListArray)