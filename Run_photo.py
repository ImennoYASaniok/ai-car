import cv2
import numpy as np

def binarize(img, d=1):
     hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
     binary_h = cv2.inRange(hls, (0, 0, 0), (255, 255, 255))

     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     binary_g = cv2.inRange(gray, 230, 255) #130

     binary = cv2.bitwise_and(binary_g, binary_h)

     if d:
         cv2.imshow('hls', hls)
         cv2.imshow('hlsRange', binary_h)
         cv2.imshow('grayRange', binary_g)
         cv2.imshow('gray', gray)
         cv2.imshow('bin', binary)

     # return binary
     return binary

# def process_frame(frame):
#     binary = binarize(frame)
#     binary1 = binary[300:250 + 210, 210:50 + 190]
#     binary2 = binary[300:250 + 210, 380:50 + 360]
#     left_line = cv2.line(binary, (400, 290), (400, 480), (150, 0, 0), 3)
#     right_line = cv2.line(binary, (235, 290), (235, 480), (150, 0, 0), 3)
#
#     if 255 in binary1:
#         print("повернуть налево!")
#     else:
#         pass
#     if 255 in binary2:
#         print("повернуть направо!")
#     else:
#         pass
#
#
#     cv2.imshow("Webcam", binary)
#     cv2.imshow("left", binary1)
#     cv2.imshow("right", binary2)
# def main():
#     cap = cv2.VideoCapture("WIN_20230827_18_05_26_Pro (online-video-cutter.com).mp4")
#
#     cap.set(3, 640)
#     cap.set(4, 480)
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         process_frame(frame)
#
#         if cv2.waitKey(1) == 27:
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
# sftp://192.168.4.4
# pi
# raspberry
# 22
# if __name__ == "__main__":
#     main()

img = cv2.imread("photo.jpg")
binary = binarize(img)
cv2.imshow("Webcam", binary)
cv2.waitKey(0)
