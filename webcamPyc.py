# Nattefrost
# escande at intechinfo.fr
# december 13 2014
# 01 taking pics from webcam


from images2gif import writeGif
import PIL
import time
import os
import sys
import pygame
import pygame.camera
import uuid

""" Checks for args given in CLI and acts accordingly """
def main(argv):
    name = str(uuid.uuid4())
    if len(argv) == 1:  # in case no arguments passed, take one picture
        print("Taking one picture")
        argv = 1
        takePic(argv, name)
    elif len(argv) == 2:
        print("Taking {} pictures".format(argv[1]))
        takePic(int(argv[1]), name)
    elif "-gif" and "-clean" in argv:
        print("Taking {} pictures and making a gif out of it".format(argv[1]))
        takePic(int(argv[1]), name)
        makeGif(name)
        cleanJpg()
    elif "-gif" in argv:
        takePic(int(argv[1]), name)
        makeGif(name)

""" Takes x pictures (.jpg) where x is given by CLI, must be first argument """
def takePic(nb, name):
    pygame.camera.init()
    pygame.camera.list_cameras()
    cam = pygame.camera.Camera("/dev/video0", (400, 400))
    cam.start()
    time.sleep(1)
    for x in range(nb):
        img = cam.get_image()
        pygame.image.save(img, "{}_{}.jpg".format(name, x))
    cam.stop()

""" Writes a gif out of all .jpg taken if -gif arg given by CLI"""
def makeGif(name):
    file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.jpg')))
    images = [PIL.Image.open(fn) for fn in file_names]
    filename = "{}.GIF".format(name)
    writeGif(filename, images, duration=0.1,repeat=True,dither=False,nq=0,dispose=3)
    print("Animated GIF generated")

""" Removes all .jpg in ./ if -clean arg given by CLI"""
def cleanJpg():
    ext = ('.jpg')
    directory = os.getcwd()
    for currentFile in os.listdir('.'):
        if currentFile.endswith(ext):
            os.remove(currentFile)
    print('Cleaned all .jpg')

if __name__ == '__main__':
    main(sys.argv)
