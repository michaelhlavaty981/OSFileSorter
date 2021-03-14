import os

path = (r'/Users/michaelhlavaty/documents')
dir_list = os.listdir(path)

def clean(filename):
    punctuation = '''!()-[]{};.:+'"\, <>/?@#$%^&*_~'''
    for i in filename:
        if i in punctuation:
            filename = filename.replace(i, "")
    filename = filename.strip()
    return filename

for file in dir_list:
    filePath = path + '/' + file
    if os.path.isfile(filePath):
        name , extension = os.path.splitext(filePath)
        newFilename = clean(file.replace(extension, "")) + extension
        os.replace(filePath, path + '/' + newFilename)