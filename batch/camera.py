#!/usr/bin/python3
import os
from picamera import PiCamera

dirname = os.path.dirname(__file__)


def capture_latest():
    full_filename = os.path.join(dirname, '../static/latest.jpg')
    with PiCamera() as camera:
        camera.capture(full_filename)


if __name__ == '__main__':
    capture_latest()
