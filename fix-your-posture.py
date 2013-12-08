#!/usr/bin/env python
# encoding: utf-8

import cv2.cv as cv
import time
import sys
import Tkinter
import tkMessageBox


SLEEP_TIME = 10


def capture_and_detect():
    capture = cv.CreateCameraCapture(-1)
    if not capture:
        print "Error: cannot create camera capture!"
        sys.exit(1)
    image = cv.QueryFrame(capture)
    if not image:
        print "Error: cannot get image!"
        sys.exit(1)

    cascade = cv.Load('haarcascade_frontalface_alt.xml')
    storage = cv.CreateMemStorage()
    faces = cv.HaarDetectObjects(image, cascade, storage)
    return faces


def show_msgbox(title, msg):
    root = Tkinter.Tk()
    root.withdraw()
    tkMessageBox.showinfo(title, msg)


def main():
    while True:
        faces = capture_and_detect()
        if not faces:
            show_msgbox("Warning", "Fix your posture now!")

        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
