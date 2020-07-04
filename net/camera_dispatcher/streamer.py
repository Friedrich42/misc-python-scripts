import base64
import os

import cv2
import zmq

IP = "127.0.0.1"
PORT = 5555

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
target_address = "tcp://{}:{}".format(IP, PORT)

print("Publishing Video to ", target_address)

footage_socket.connect(target_address)

camera = cv2.VideoCapture("rtsp://admin:Test1234@192.168.5.61:554/onvif1")  # init the camera

print("Started streaming video")
while True:
    try:
        _, buffer = camera.read()
        buffer_encoded = base64.b64encode(buffer)
        footage_socket.send(buffer_encoded)
        # Update the FPS counter
        cv2.waitKey(113)
    except KeyboardInterrupt:
        # stop the timer and display FPS information
        camera.release()
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break

