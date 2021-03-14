import os, shutil, time

while True:
    os.chdir(r'/Users/michaelhlavaty/Desktop')
    path = os.getcwd()
    dir_list = os.listdir(path)
    for file in dir_list:
        print(path + '/' + file)
        os.rename(path + "/" + file, '/Users/michaelhlavaty/documents/' + file)
    time.sleep(10)
