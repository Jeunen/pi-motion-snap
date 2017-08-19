#!/usr/bin/python

import time
from includes.picture import Picture
from includes.just_email import JustEmail
from includes.pusher_trigger import PusherTrigger
from gpiozero import MotionSensor
from settings import general

class Main:

    def __init__(self):

        pic = Picture()
        pusher = PusherTrigger()
        pir = MotionSensor(4)

        while True:
            if pir.motion_detected:

                pusher.shoot()
                email = JustEmail()
                email.make_message()
                images = []

                for i in range(0, general['PIC_AMOUNT']):
                    name = pic.create_name()
                    pic.take_pic(name)
                    images.append(name)
                    time.sleep(general['INTERVAL'])

                email.add_images(images)
                email.send_mail()


if __name__ == "__main__":
    Main()
