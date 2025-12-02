import cv2
import cv2 as cv
import numpy as np
from time import *
import os
import queue
from threading import *
import pigpio

ESC = 17  # пин контроллера двигателя (нумерация BCM)
STEER = 18  # пин сервопривода (нумерация BCM)


def setup_gpio():
    os.system("sudo pigpiod")  # Launching GPIO library
    time.sleep(1)
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(ESC, 0)
    pi.set_servo_pulsewidth(STEER, 0)
    time.sleep(1)
    # pi.set_servo_pulsewidth(ESC, 1500)
    # time.sleep(1)
    return pi


def control(pi, ESC, speed, STEER, angle):
    pi.set_servo_pulsewidth(ESC, speed)
    pi.set_servo_pulsewidth(STEER, int(16.6666666 * angle))


def binarize(frame):
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    binary_h = cv2.inRange(hls, (0, 0, 0), (255, 255, 255))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary_g = cv2.inRange(gray, 230, 255)  # 23C

    binary = cv2.bitwise_and(binary_g, binary_h)
    gaus = cv2.GaussianBlur(binary, (3, 3), 5)
    canny = cv2.Canny(gaus, 270, 320)

    # return binary
    return canny


def process_frame(frame=None, pid=None):
    binary = binarize(frame)
    binary1 = binary[300:250 + 210, 210:50 + 190]
    binary2 = binary[300:250 + 210, 380:50 + 360]
    cv2.line(binary, (400, 290), (400, 480), (150, 0, 0), 3)
    cv2.line(binary, (235, 290), (235, 480), (150, 0, 0), 3)
    if 255 in binary1:
        print("повернуть налево!")
        control(pid, ESC, 560, STEER, 90 - 7)
    elif 255 in binary2:
        print("повернуть направо!")
        control(pid, ESC, 560, STEER, 90 + 7)
    else:
        control(pid, ESC, 1550, STEER, 90)
    # cv2.imshow("Webcam", binary)


def config():
    # Настройка параметров камеры
    # Закомментируйте по желанию
    os.system('v4l2-ctl -d /dev/video0 --list-ctrls')
    time.sleep(1)
    os.system('v4l2-ctl -d /dev/video0 -c exposure_auto=1')
    os.system('v4l2-ctl -d /dev/video0 -c exposure_absolute=200')
    time.sleep(1)
    os.system('v4l2-ctl -d /dev/video0 --list-ctrls')
    time.sleep(1)


def general_loop():
    config()
    pi = setup_gpio()
    control(pi, ESC, 1500, STEER, 90)
    time.sleep(1)

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while cap.isOpened():
        try:
            # frame = VS.read()
            ret, frame = cap.read()
            j += 1
            if j > 25:
                newTimej = time.time()
                lastTimej = newTimej
                j = 0
            process_frame(frame=frame, pid=pi)
            time.sleep(0.01)
        except KeyboardInterrupt:
            control(pi, ESC, 1500, STEER, 90)
            break
    cap.release()


if __name__ == '__main__':
    general_loop()