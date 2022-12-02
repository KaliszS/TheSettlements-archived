import os

def get_filename(fileObject):
    path = os.path.basename(fileObject)
    full_filename_tuple = os.path.splitext(path)
    filename = full_filename_tuple [0]

    return filename