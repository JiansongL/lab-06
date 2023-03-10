import grovepi
from grove_rgb_lcd import *

setRGB(0, 255, 0)
setText("Welcome")
flag = 1

while True:
        time.sleep(0.5)
        threshold_dis = grovepi.analogRead(0)
        ultrasonic_dis = grovepi.ultrasonicRead(2)

        if ultrasonic_dis >= threshold_dis:
                setRGB(0, 255, 0)
                if  flag != 0:
                        flag = 0
                        setText(f"{threshold_dis} cm \n{ultrasonic_dis} cm")
                else:
                        setText_norefresh(f"{threshold_dis} cm \n{ultrasonic_dis} cm$
        else:
                setRGB(255, 0 ,0)
                setText_norefresh(f"{threshold_dis} cm OBJ PRES \n{ultrasonic_dis} c$
                flag = 1
