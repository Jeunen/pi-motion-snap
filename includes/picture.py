from picamera import PiCamera
from datetime import datetime
from settings import picture


class Picture:

    def __init__(self):
        self.camera = PiCamera()
        self.folder = picture["FOLDER"]
        self.timeformat = picture["TIMEFORMAT"]

    def create_name(self):
        try:
            if self.folder:
                return datetime.now().strftime(self.folder + "/" + self.timeformat)
            else:
                return datetime.now().strftime(self.timeformat)
        except Exception as e:
            print("createname " + str(e))

    def take_pic(self, name):
        try:
            self.camera.capture(name)
            print("pic taken.")

        except picamera.exc.PiCameraError as e:
            print("takepic " + str(e))
