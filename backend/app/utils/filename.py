import os

def getFileName(fileObject):
    path = os.path.basename(fileObject)
    fullFilenameTuple = os.path.splitext(path)
    filename = fullFilenameTuple[0]

    return filename