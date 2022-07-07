from PIL import Image

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